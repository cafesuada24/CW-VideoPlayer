DROP TABLE IF EXISTS videos;
DROP TABLE IF EXISTS playlist;
DROP TABLE IF EXISTS playlist_video;

CREATE TABLE videos (
  video_id   INTEGER      PRIMARY KEY,
  name       VARCHAR(255) NOT NULL,
  director   VARCHAR(255) DEFAULT 'Unknown',
  rating     INTEGER      DEFAULT 0,
  play_count INTEGER      DEFAULT 0,
  file_path  VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE playlist (
  playlist_id INTEGER      PRIMARY KEY,
  name        VARCHAR(255) NOT NULL
); 

CREATE TABLE playlist_video (
  video_id    INTEGER NOT NULL,
  playlist_id INTEGER NOT NULL,
  FOREIGN KEY (video_id)
  REFERENCES videos (video_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  FOREIGN KEY (playlist_id)
  REFERENCES playlist (playlist_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

INSERT INTO videos (name, director, rating, file_path) 
VALUES
(
  'Ambient Nature Atmostphere',
  'Ambient Nature',
  3,
  '/home/serein/programming/Projects/CW_VideoPlayer/resources/videos/ambient_nature.mp4'
),
(
  'Love',
  'Peggy Anke',
  2,
  '/home/serein/programming/Projects/CW_VideoPlayer/resources/videos/love.mp4'
),
(
  'Short Video 3',
  'Codix Damiyen',
  4,
  '/home/serein/programming/Projects/CW_VideoPlayer/resources/videos/short_video_3.mp4'
);

INSERT INTO playlist (name)
VALUES (
  'all'
);

INSERT INTO playlist_video (video_id, playlist_id)
VALUES
(1, 1),
(2, 1),
(3, 1);
