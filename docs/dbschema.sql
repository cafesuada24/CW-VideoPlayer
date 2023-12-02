DROP TABLE IF EXISTS videos;

CREATE TABLE videos (
  video_id   INTEGER      PRIMARY KEY,
  name       VARCHAR(255) NOT NULL,
  director   VARCHAR(255) DEFAULT 'Unknown',
  rating     INTEGER      DEFAULT 0,
  play_count INTEGER      DEFAULT 0,
  file_path  VARCHAR(255) NOT NULL UNIQUE
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
),
(
  'Blah',
  'haha',
  2,
  '/home/serein/programming/Projects/CW_VideoPlayer/resources/videos/haha.mp4'
);
