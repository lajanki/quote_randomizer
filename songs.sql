--song lyrics for the randomizer in separate tables

-- Status table for
--  -user: name whose status to read (given to a SongRandomizer object)
--  -song: one of the tables below
--  -current_row: row index of the next row to read
CREATE TABLE song_status (name TEXT NOT NULL UNIQUE, song TEXT, current_row INTEGER);

--Californication
CREATE TABLE [Red Hot Chili Peppers - Californication](verse TEXT NOT NULL)
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('Psychic spies from China try to steal your mind''s elation');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('Little girls from Sweden dream of silver screen quotations');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('And if you want these kind of dreams it''s Californication');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('It''s the edge of the world and all of western civilization');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('The sun may rise in the East at least it settles in the final location');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('It''s understood that Hollywood sells Californication');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('Pay your surgeon very well to break the spell of aging');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('Celebrity skin is this your chin or is that war your waging');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('First born unicorn hard core soft porn');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('Dream of Californication, dream of Californication');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('Marry me girl be my fairy to the world be my very own constellation');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('A teenage bride with a baby inside getting high on information');

INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('And buy me a star on the boulevard it''s Californication');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('Space may be the final frontier but it''s made in a Hollywood basement');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('Cobain can you hear the spheres singing songs off station to station');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('And Alderon''s not far away it''s Californication');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('Born and raised by those who praise control of population everybody''s been there and I don''t mean on vacation');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('Destruction leads to a very rough road but it also breeds creation');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('And earthquakes are to a girl''s guitar they''re just another good vibration');

INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('And tidal waves couldn''t save the world from Californication');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('Pay your surgeon very well to break the spell of aging');
INSERT INTO [Red Hot Chili Peppers - Californication](verse) VALUES ('Sicker than the rest there is no test but this is what you''re craving');

--Stairway to Heaven
CREATE TABLE [Led Zeppelin - Stairway to Heaven](verse TEXT NOT NULL)
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('There''s a lady who''s sure all that glitters is gold');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('And she''s buying a stairway to heaven. When she gets there she knows, if the stores are all closed');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('With a word she can get what she came for. And she''s buying a stairway to heaven.');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('There''s a sign on the wall but she wants to be sure');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('Cause you know sometimes words have two meanings.');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('In a tree by the brook, there''s a songbird who sings, sometimes all of our thoughts are misgiven.');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('Ooh, it makes me wonder, ooh, it makes me wonder.');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('There''s a feeling I get when I look to the west, and my spirit is crying for leaving.');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('In my thoughts I have seen rings of smoke through the trees, and the voices of those who stand looking.');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('Ooh, it makes me wonder, ooh, it really makes me wonder.');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('And it''s whispered that soon, if we all call the tune, then the piper will lead us to reason.');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('And a new day will dawn for those who stand long, and the forests will echo with laughter.');

INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('If there''s a bustle in your hedgerow, don''t be alarmed now, it''s just a spring clean for the May queen.');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('Yes, there are two paths you can go by, but in the long run');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('There''s still time to change the road you''re on. And it makes me wonder.');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('Your head is humming and it won''t go, in case you don''t know, the piper''s calling you to join him,');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('Dear lady, can you hear the wind blow, and did you know your stairway lies on the whispering wind?');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('And as we wind on down the road our shadows taller than our soul.');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('There walks a lady we all know who shines white light and wants to show');

INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('How everything still turns to gold. And if you listen very hard');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('The tune will come to you at last. When all are one and one is all');
INSERT INTO [Led Zeppelin - Stairway to Heaven](verse) VALUES ('To be a rock and not to roll. And she''s buying a stairway to heaven.');

--How Can I Tell You?
CREATE TABLE [Cat Stevens - How Can I Tell You?](verse TEXT NOT NULL)
INSERT INTO [Cat Stevens - How Can I Tell You?](verse) VALUES ('How can I tell you that I love you, I love you');
INSERT INTO [Cat Stevens - How Can I Tell You?](verse) VALUES ('But I can''t think of right words to say, I long to tell you that I''m always thinking of you');
INSERT INTO [Cat Stevens - How Can I Tell You?](verse) VALUES ('I''m always thinking of you, but my words just blow away, just blow away');
INSERT INTO [Cat Stevens - How Can I Tell You?](verse) VALUES ('It always ends up to one thing, honey and I can''t think of right words to say');
INSERT INTO [Cat Stevens - How Can I Tell You?](verse) VALUES ('Wherever I am girl, I''m always walking with you I''m always walking with you, but I look and you''re not there');
INSERT INTO [Cat Stevens - How Can I Tell You?](verse) VALUES ('Whoever I''m with, I''m always, always talking to you I''m always talking to you, and I''m sad that');
INSERT INTO [Cat Stevens - How Can I Tell You?](verse) VALUES ('You can''t hear, sad that you can''t hear it always ends up to one thing, honey,');
INSERT INTO [Cat Stevens - How Can I Tell You?](verse) VALUES ('When I look and you''re not there I need to know you, need to feel my arms around you');
INSERT INTO [Cat Stevens - How Can I Tell You?](verse) VALUES ('Feel my arms around you, like a sea around a shore and each night and day I pray, in hope');
INSERT INTO [Cat Stevens - How Can I Tell You?](verse) VALUES ('That I might find you, in hope that I might find you, because heart''s can do no more');
INSERT INTO [Cat Stevens - How Can I Tell You?](verse) VALUES ('It always ends up to one thing honey, still I kneel upon the floor how can I tell you that I love you, I love you');
INSERT INTO [Cat Stevens - How Can I Tell You?](verse) VALUES ('But I can''t think of right words to say I long to tell you that I''m always thinking of you');
INSERT INTO [Cat Stevens - How Can I Tell You?](verse) VALUES ('I''m always thinking of you... It always ends up to one thing honey and I can''t think of right words to say');

--The Zen of Python
CREATE TABLE [The Zen of Python](verse TEXT NOT NULL)
INSERT INTO [The Zen of Python](verse) VALUES ('Beatiful is better than ugly.');
INSERT INTO [The Zen of Python](verse) VALUES ('Explicit is better than implicit.');
INSERT INTO [The Zen of Python](verse) VALUES ('Simple is better than complex.' );
INSERT INTO [The Zen of Python](verse) VALUES ('complex is better than complicated.' );
INSERT INTO [The Zen of Python](verse) VALUES ('Flat is better than nested.' );
INSERT INTO [The Zen of Python](verse) VALUES ('Sparse is better than dense.' );
INSERT INTO [The Zen of Python](verse) VALUES ('Readability counts.' );
INSERT INTO [The Zen of Python](verse) VALUES ('Special cases aren''t special enough to break the rules.' );
INSERT INTO [The Zen of Python](verse) VALUES ('Although practicality beats purity.' );
INSERT INTO [The Zen of Python](verse) VALUES ('Errors should never pass silently.' );
INSERT INTO [The Zen of Python](verse) VALUES ('Unless explicitly silenced.' );
INSERT INTO [The Zen of Python](verse) VALUES ('In the face of ambiguity, refuse the temptation to guess.');
INSERT INTO [The Zen of Python](verse) VALUES ('There should be one, and preferably only one, obvious way to do it.' );
INSERT INTO [The Zen of Python](verse) VALUES ('Although that way may not be obvious at first unless you''re Dutch.');
INSERT INTO [The Zen of Python](verse) VALUES ('Now is better than never.' );
INSERT INTO [The Zen of Python](verse) VALUES ('Although never is often better than right now.' );
INSERT INTO [The Zen of Python](verse) VALUES ('If the implementation is hard to explain, it''s a bad idea.' );
INSERT INTO [The Zen of Python](verse) VALUES ('If the implementation is easy to explain, it may be a good idea.' );
INSERT INTO [The Zen of Python](verse) VALUES ('Namespaces are one honking great idea - let''s do more of those!');

--Nights in white satin
CREATE TABLE [Moody Blues - Nights in White Satin](verse TEXT NOT NULL)
INSERT INTO [Moody Blues - Nights in White Satin](verse) VALUES ('Nights in white satin never reaching the end.');
INSERT INTO [Moody Blues - Nights in White Satin](verse) VALUES ('Letters I''ve written never meaning to send.');
INSERT INTO [Moody Blues - Nights in White Satin](verse) VALUES ('Beauty I''ve always missed With these eyes before.' );
INSERT INTO [Moody Blues - Nights in White Satin](verse) VALUES ('Just what the truth is I can''t say any more.' );
INSERT INTO [Moody Blues - Nights in White Satin](verse) VALUES ('Cause I love you, yes I love you. Oh how I love you.' );
INSERT INTO [Moody Blues - Nights in White Satin](verse) VALUES ('Gazing at people some hand in hand just what I''m going through they can''t understand.' );
INSERT INTO [Moody Blues - Nights in White Satin](verse) VALUES ('Some try to tell me thoughts they cannot defend. Just what you want to be you will be in the end.' );
INSERT INTO [Moody Blues - Nights in White Satin](verse) VALUES ('And I love you, yes I love you.' );
INSERT INTO [Moody Blues - Nights in White Satin](verse) VALUES ('Oh how I love you, oh how I love you.' );
INSERT INTO [Moody Blues - Nights in White Satin](verse) VALUES ('Nights in white satin never reaching the end.' );
INSERT INTO [Moody Blues - Nights in White Satin](verse) VALUES ('Letters I''ve written never meaning to send.' );
INSERT INTO [Moody Blues - Nights in White Satin](verse) VALUES ('Beauty I''ve always missed With these eyes before.');
INSERT INTO [Moody Blues - Nights in White Satin](verse) VALUES ('Just what the truth is I can''t say any more.' );
INSERT INTO [Moody Blues - Nights in White Satin](verse) VALUES ('Cause I love you, yes I love you. Oh how I love you, oh how I love you.');

--What a Wonderful World
CREATE TABLE [Louis Armstrong - What a Wonderful World](verse TEXT NOT NULL)
INSERT INTO [Louis Armstrong - What a Wonderful World](verse) VALUES ('I see trees of green, red roses too.');
INSERT INTO [Louis Armstrong - What a Wonderful World](verse) VALUES ('I see them bloom for me and you and I think to myself what a wonderful world.' );
INSERT INTO [Louis Armstrong - What a Wonderful World](verse) VALUES ('I see skies of blue and clouds of white. The bright blessed day, the dark sacred night.' );
INSERT INTO [Louis Armstrong - What a Wonderful World](verse) VALUES ('And I think to myself what a wonderful world.' );
INSERT INTO [Louis Armstrong - What a Wonderful World](verse) VALUES ('The colors of the rainbow so pretty in the sky, are also on the faces of people going by.' );
INSERT INTO [Louis Armstrong - What a Wonderful World](verse) VALUES ('I see friends shaking hands saying how do you do, but they''re really saying I love you.' );
INSERT INTO [Louis Armstrong - What a Wonderful World](verse) VALUES ('I hear baby''s crying and I watched them grow, they''ll learn much more than I''ll ever know.' );
INSERT INTO [Louis Armstrong - What a Wonderful World](verse) VALUES ('And I think to myself what a wonderful world. Yes, I think to myself what a wonderful world.');

--Behind Blue Eyes
CREATE TABLE [Limp Bizkit - Behind Blue Eyes](verse TEXT NOT NULL)
INSERT INTO [Limp Bizkit - Behind Blue Eyes](verse) VALUES ('No one knows what it''s like to be the bad man, to be the sad man. Behind blue eyes.');
INSERT INTO [Limp Bizkit - Behind Blue Eyes](verse) VALUES ('And no one knows what it''s like to be hated, to be fated to telling only lies.' );
INSERT INTO [Limp Bizkit - Behind Blue Eyes](verse) VALUES ('But my dreams they aren''t as empty as my conscience seems to be.' );
INSERT INTO [Limp Bizkit - Behind Blue Eyes](verse) VALUES ('I have hours, only lonely. My love is vengeance that''s never free.' );
INSERT INTO [Limp Bizkit - Behind Blue Eyes](verse) VALUES ('No one knows what its like to feel these feelings like I do, and I blame you!' );
INSERT INTO [Limp Bizkit - Behind Blue Eyes](verse) VALUES ('No one bites back as hard on their anger.' );
INSERT INTO [Limp Bizkit - Behind Blue Eyes](verse) VALUES ('None of my pain and woe can show through.' );
INSERT INTO [Limp Bizkit - Behind Blue Eyes](verse) VALUES ('No one knows what its like to be mistreated, to be defeated behind blue eyes.' );
INSERT INTO [Limp Bizkit - Behind Blue Eyes](verse) VALUES ('No one knows how to say that they''re sorry and don''t worry. I''m not telling lies.' );
INSERT INTO [Limp Bizkit - Behind Blue Eyes](verse) VALUES ('No one knows what its like to be the bad man, to be the sad man. Behind blue eyes.');

--Yesterday
CREATE TABLE [The Beatles - Yesterday](verse TEXT NOT NULL)
INSERT INTO [The Beatles - Yesterday](verse) VALUES ('Yesterday all my troubles seemed so far away.');
INSERT INTO [The Beatles - Yesterday](verse) VALUES ('Now it looks as though they''re here to stay. Oh, I believe in yesterday.' );
INSERT INTO [The Beatles - Yesterday](verse) VALUES ('Suddenly I''m not half the man I used to be. There''s a shadow hanging over me. Oh, yesterday came suddenly.' );
INSERT INTO [The Beatles - Yesterday](verse) VALUES ('Why she had to go, I don''t know, she wouldn''t say. I said something wrong, now I long for yesterday.' );
INSERT INTO [The Beatles - Yesterday](verse) VALUES ('Yesterday love was such an easy game to play. Now I need a place to hide away. Oh, I believe in yesterday.' );
INSERT INTO [The Beatles - Yesterday](verse) VALUES ('Why she had to go, I don''t know, she wouldn''t say. I said something wrong, now I long for yesterday.' );
INSERT INTO [The Beatles - Yesterday](verse) VALUES ('Yesterday love was such an easy game to play.' );
INSERT INTO [The Beatles - Yesterday](verse) VALUES ('Now I need a place to hide away. Oh, I believe in yesterday.');
