CREATE TABLE gravadora (
id_grav uniqueidentifier NOT NULL,
website varchar(50) NOT NULL,
nome varchar(50) NOT NULL,
ender varchar(50) NOT NULL,

CONSTRAINT Pk_gravadora
PRIMARY KEY (id_grav)
)
on BDspotper_fg01;

CREATE TABLE telefone_gravadora (
telefone bigint NOT NULL,
id_grav uniqueidentifier NOT NULL,

CONSTRAINT Pk_telefone_gravadora
PRIMARY KEY (id_grav),

CONSTRAINT Fk_telefone_gravadora
FOREIGN KEY (id_grav) REFERENCES gravadora(id_grav)
ON UPDATE CASCADE
)
on BDspotper_fg01;

--ALTER TABLE telefone_gravadora
--ALTER COLUMN telefone bigint NOT NULL;

CREATE TABLE album (
id_album uniqueidentifier NOT NULL,
id_grav uniqueidentifier NOT NULL,
descricao varchar(100) NOT NULL,
tipo_compra varchar(50) NOT NULL,
preco dec(5,2) NOT NULL,
data_compra date NOT NULL,
data_gravacao date NOT NULL,
meio_fisico varchar(10),
tipo_grav_cd varchar(5),

CONSTRAINT check_meio_fisico_tipo_grav_cd CHECK (
  (meio_fisico = 'CD' AND tipo_grav_cd IN ('ADD', 'DDD')) OR
  (meio_fisico IN ('DOWNLOAD', 'VINIL') AND tipo_grav_cd IS NULL)),


CONSTRAINT Pk_album PRIMARY KEY (id_album),

CONSTRAINT Fk_album_gravadora
FOREIGN KEY (id_grav) REFERENCES gravadora(id_grav)
ON UPDATE CASCADE
ON DELETE NO ACTION
) 
on BDspotper_fg01;


CREATE TABLE tipo_composicao (
id_tipo_comp uniqueidentifier NOT NULL,
descricao varchar(100) NOT NULL,

CONSTRAINT Pk_tipo_comp
PRIMARY KEY (id_tipo_comp)
)
on BDspotper_fg01;


CREATE TABLE faixa (
id_faixa uniqueidentifier NOT NULL,
id_album uniqueidentifier NOT NULL,
id_tipo_comp uniqueidentifier NOT NULL,
descricao varchar(100) NOT NULL,
tempo_de_exec time NOT NULL,
pos_album int NOT NULL,
num_cd smallint,
num_vinil smallint,

CONSTRAINT pk_faixa PRIMARY KEY NONCLUSTERED (id_faixa),

CONSTRAINT Fk_faixa_album
FOREIGN KEY (id_album) REFERENCES album(id_album)
ON UPDATE CASCADE
ON DELETE NO ACTION,

CONSTRAINT Fk_faixa_tipo_comp
FOREIGN KEY (id_tipo_comp) REFERENCES tipo_composicao(id_tipo_comp)
ON UPDATE CASCADE
ON DELETE NO ACTION
)
on BDspotper_fg02;

CREATE TABLE periodo_musical (
id_periodo_musical uniqueidentifier NOT NULL,
descricao varchar(50) NOT NULL,
data_inicio date NOT NULL,
data_fim date NOT NULL,

CONSTRAINT Pk_periodo_musical
PRIMARY KEY (id_periodo_musical)
)
on BDspotper_fg01;

CREATE TABLE compositor (
id_compositor uniqueidentifier NOT NULL,
id_periodo_musical uniqueidentifier NOT NULL,
nome varchar(50) NOT NULL,
local_nasc varchar(50) NOT NULL,
data_nasc date NOT NULL,
data_morte date,

CONSTRAINT Pk_compositor
PRIMARY KEY (id_compositor),

CONSTRAINT Fk_compositor_per_musical
FOREIGN KEY (id_periodo_musical) REFERENCES periodo_musical(id_periodo_musical)
ON UPDATE CASCADE
ON DELETE NO ACTION
)
on BDspotper_fg01;

Create table faixa_compositor
(
id_faixa uniqueidentifier not null,
id_compositor uniqueidentifier not null,

constraint pk_faixa_compositor
primary key (id_compositor, id_faixa),

constraint fk_compositor
foreign key (id_compositor) references compositor (id_compositor)
on update cascade
on delete no action,

CONSTRAINT FK_faixa_compositor_faixa FOREIGN KEY (id_faixa) REFERENCES Faixa (id_faixa) ON DELETE CASCADE
on update cascade
)
on BDspotper_fg01;


Create table interprete
(
id_interprete uniqueidentifier not null,
nome varchar(50) not null,
tipo varchar (50) not null,

constraint pk_id_interprete
primary key (id_interprete)
)
on BDspotper_fg01;

CREATE TABLE faixa_interprete (
id_faixa uniqueidentifier NOT NULL,
id_interprete uniqueidentifier NOT NULL,

CONSTRAINT Pk_faixa_interprete
PRIMARY KEY (id_faixa, id_interprete),

CONSTRAINT Fk_interprete_faixa
FOREIGN KEY (id_interprete) REFERENCES interprete(id_interprete)
ON UPDATE CASCADE
ON DELETE NO ACTION,

CONSTRAINT FK_faixa_interprete_faixa FOREIGN KEY (id_faixa) REFERENCES faixa(id_faixa) ON DELETE CASCADE

) 
on BDspotper_fg01;

CREATE TABLE playlist
(
id_playlist uniqueidentifier NOT NULL,
nome varchar(50) NOT NULL,
data_criacao date not null,
tempo_total_exec time not null,

CONSTRAINT Pk_playlist
PRIMARY KEY (id_playlist)
)
on BDspotper_fg02;


CREATE TABLE faixa_playlist
(
id_playlist uniqueidentifier NOT NULL,
id_faixa uniqueidentifier not null,

CONSTRAINT Pk_faixa_playlist
PRIMARY KEY (id_playlist, id_faixa),

CONSTRAINT Fk_playlist
FOREIGN KEY (id_playlist) REFERENCES playlist(id_playlist)
ON UPDATE CASCADE
ON DELETE NO ACTION,

CONSTRAINT FK_faixa_playlist_faixa FOREIGN KEY (id_faixa) REFERENCES faixa(id_faixa) ON DELETE CASCADE
ON UPDATE CASCADE  
)
on BDspotper_fg02;

CREATE CLUSTERED INDEX FAIXA_ID_ALBUM ON FAIXA (id_album) with (pad_index=on, fillfactor=100);

CREATE NONCLUSTERED INDEX ID_TIPO_COMPOS_FAIXA
ON FAIXA (id_tipo_comp)
WITH (FILLFACTOR = 100, PAD_INDEX = ON);


