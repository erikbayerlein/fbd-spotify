--5) Criar uma visão materializada que tem como atributos o nome da playlist e a
--quantidade de álbuns que a compõem.
CREATE VIEW dbo.Rel_item5 (Nome_PL, QDE_Album) 
WITH SCHEMABINDING
AS
SELECT pl.nome as Nome_PL, count_big (a.id_album) as QDE_Album
FROM dbo.playlist pl 
INNER JOIN dbo.faixa_playlist fpl ON pl.id_playlist = fpl.id_playlist
INNER JOIN dbo.faixa f ON fpl.id_faixa = f.id_faixa
INNER JOIN dbo.album a ON f.id_album = a.id_album
GROUP BY pl.nome;

-- nao funciona por nada
CREATE UNIQUE CLUSTERED INDEX Item_5p2
ON dbo.Rel_item5 (Nome_Playlist);


--6) Defina uma função que tem como parâmetro de entrada o nome (ou parte do)
--nome do compositor e o parâmetro de saída todos os álbuns com obras
--compostas pelo compositor.

CREATE FUNCTION dbo.Obras_do_Compositor(@nome_comp VARCHAR(50))
RETURNS TABLE
AS
RETURN 
(
   SELECT a.descricao as NomeAlbum, f.descricao as Faixas
   FROM album a
   INNER JOIN faixa f ON a.id_album = f.id_album
   INNER JOIN faixa_compositor fc ON f.id_faixa = fc.id_faixa
   INNER JOIN compositor c on fc.id_compositor = c.id_compositor
   WHERE c.nome LIKE '%' + @nome_comp + '%'
   GROUP BY a.descricao, f.descricao
);

CREATE FUNCTION dbo.Album_do_Comp(@nome_comp VARCHAR(50))
RETURNS TABLE
AS
RETURN 
(
   SELECT a.id_album as Id_Album, f.descricao as Faixas
   FROM album a
   INNER JOIN faixa f ON a.id_album = f.id_album
   INNER JOIN faixa_compositor fc ON f.id_faixa = fc.id_faixa
   INNER JOIN compositor c on fc.id_compositor = c.id_compositor
   WHERE c.nome LIKE '%' + @nome_comp + '%'
   GROUP BY a.id_album, f.descricao
);

----------------------------------------------------------------


-- gatilho do delete faixa da playlist
CREATE TRIGGER trg_update_playlist_tempo_total_exec_delete
ON faixa_playlist
AFTER DELETE
AS
BEGIN
 DECLARE @id_playlist uniqueidentifier, @tempo_total_exec_seconds INT, @sum_seconds INT

 SELECT @id_playlist = id_playlist FROM deleted

 SELECT @tempo_total_exec_seconds = DATEDIFF(SECOND, '00:00:00', tempo_total_exec)
 FROM playlist
 WHERE id_playlist = @id_playlist

 SELECT @sum_seconds = SUM(DATEDIFF(SECOND, '00:00:00', tempo_de_exec))
 FROM faixa
 WHERE id_faixa IN (SELECT id_faixa FROM deleted)

 SET @tempo_total_exec_seconds = @tempo_total_exec_seconds - @sum_seconds

 DECLARE @sum_time TIME
 SET @sum_time = DATEADD(SECOND, @tempo_total_exec_seconds, '00:00:00')

 UPDATE playlist
 SET tempo_total_exec = @sum_time
 WHERE id_playlist = @id_playlist
END


-----------

CREATE TRIGGER trg_update_playlist_tempo_total_exec
ON faixa_playlist
AFTER INSERT
AS
BEGIN
 DECLARE @id_playlist uniqueidentifier, @tempo_total_exec_seconds INT, @tempo_de_exec_seconds INT, @sum_seconds INT

 SELECT @id_playlist = id_playlist FROM inserted

 SELECT @tempo_total_exec_seconds = DATEDIFF(SECOND, '00:00:00', tempo_total_exec)
 FROM playlist
 WHERE id_playlist = @id_playlist

 SELECT @tempo_de_exec_seconds = DATEDIFF(SECOND, '00:00:00', tempo_de_exec)
 FROM faixa
 WHERE id_faixa IN (SELECT id_faixa FROM inserted)

 SET @sum_seconds = @tempo_total_exec_seconds + @tempo_de_exec_seconds

 DECLARE @sum_time TIME
 SET @sum_time = DATEADD(SECOND, @sum_seconds, '00:00:00')

 UPDATE playlist
 SET tempo_total_exec = @sum_time
 WHERE id_playlist = @id_playlist
END

---- 
CREATE PROCEDURE DeleteAlbum @id_album uniqueidentifier
AS
BEGIN
 DELETE FROM faixa_compositor WHERE id_faixa IN (SELECT id_faixa FROM faixa WHERE id_album = @id_album)
 DELETE FROM faixa_interprete WHERE id_faixa IN (SELECT id_faixa FROM faixa WHERE id_album = @id_album)
 DELETE FROM faixa_playlist WHERE id_faixa IN (SELECT id_faixa FROM faixa WHERE id_album = @id_album)
 DELETE FROM faixa WHERE id_album = @id_album
 DELETE FROM album WHERE id_album = @id_album
END

-- EXEC DeleteAlbum @id_album = 12

CREATE TRIGGER trg_album64Faixas
ON faixa
FOR INSERT, UPDATE
AS
BEGIN
   IF EXISTS (
       SELECT 1
       FROM inserted i
       JOIN faixa f ON i.id_album = f.id_album
       GROUP BY f.id_album
       HAVING COUNT(f.id_faixa) > 64
   )
   BEGIN
       RAISERROR ('Erro: Um album só pode ter no maximo 64 faixas', 16, 1);
       ROLLBACK TRANSACTION;
       RETURN;
   END;
END;

------------------

CREATE TRIGGER trg_barrocoTres
ON faixa_compositor
INSTEAD OF INSERT
AS
BEGIN
  SET NOCOUNT ON;

  IF EXISTS (
    SELECT 1
    FROM inserted i
    JOIN faixa f ON i.id_faixa = f.id_faixa
    JOIN album a ON f.id_album = a.id_album AND (a.tipo_grav_cd = 'ADD' OR a.meio_fisico = 'vinil' OR a.meio_fisico = 'download')
    JOIN compositor c ON c.id_compositor = i.id_compositor
    JOIN periodo_musical pm ON pm.id_periodo_musical = c.id_periodo_musical AND pm.descricao = 'Barroco'
  )
  BEGIN
    DECLARE @id_deletar UNIQUEIDENTIFIER;
    SELECT TOP 1 @id_deletar = a.id_album
    FROM inserted i
    JOIN faixa f ON i.id_faixa = f.id_faixa
    JOIN album a ON a.id_album = f.id_album;

    EXEC DeleteAlbum @id_album = @id_deletar;

    RAISERROR ('Erro: Se a composicao eh do estilo Barroco, a gravacao precisa ser em cd DDD. A insercao nao foi realizada e o album informado foi excluido junto com as faixas nao autorizadas', 16, 1);

    RETURN;
  END
  ELSE
  BEGIN
    INSERT INTO faixa_compositor
    SELECT * FROM inserted;
  END;
END;


CREATE TRIGGER trg_preco_album
ON album
FOR INSERT, UPDATE
AS
BEGIN
   IF EXISTS (
       SELECT 1
       FROM inserted i
       WHERE i.preco > 3*(SELECT AVG(a.preco) FROM album a)
   )
   BEGIN
       RAISERROR ('Erro: o preco de um album nao pode ser 3x o valor da média dos preços já existentes', 16, 1);
       ROLLBACK TRANSACTION;
       RETURN;
   END;
END;

