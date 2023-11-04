DROP TABLE IF EXISTS videos;

CREATE TABLE videos (
  video_id   INTEGER      PRIMARY KEY,
  name       VARCHAR(255) NOT NULL,
  author     VARCHAR(255) DEFAULT 'Unknown',
  rating     INTEGER      DEFAULT 0,
  play_count INTEGER      DEFAULT 0,
  file_name  VARCHAR(255) NOT NULL UNIQUE
);

INSERT INTO videos (name, author, rating, file_name) 
VALUES (
  'Ambient Nature Atmostphere',
  'Ambient Nature',
  3,
  'ambient_nature.mp4'
);

INSERT INTO videos (name, author, rating, file_name)
VALUES (
  'Love',
  'Peggy Anke',
  2,
  'love.mp4'
);

INSERT INTO videos (name, author, rating, file_name)
VALUES (
  'Short Video 3',
  'Codix Damiyen',
  4,
  'short_video_3.mp4'
);
