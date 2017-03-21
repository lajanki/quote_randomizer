--A collection of quotes, lyrics and such for creating the quotes and lyrics table for the database.
--Note: does not create the dictionary table.

--sources:
--http://www.forbes.com/sites/kevinkruse/2013/05/28/inspirational-quotes/
--http://www.cs.virginia.edu/~robins/quotes.html
--http://www.quotery.com/lists/top-500-greatest-quotes-of-all-time/
--http://www.inc.com/lolly-daskal/100-motivational-quotes-that-will-inspire-you-to-succeed.html
--http://www.notable-quotes.com/
--https://www.spec2000.net/06-basicphysics.htm
--http://www.quotegarden.com/
--http://www.adslogans.co.uk/site/pages/home/hall-of-fame.php
--http://www.hongkiat.com/blog/77-catchy-and-creative-slogans/
--http://www.goodreads.com/topic/show/1006385-1-000-random-facts
--https://www.reddit.com/r/quotes/


--DROP TABLE IF EXISTS quotes;  --data is no longer DROPPED!
--CREATE TABLE quotes (quote TEXT UNIQUE NOT NULL, author TEXT NOT NULL, frequency INTEGER DEFAULT 0);


INSERT INTO quotes(quote, author) VALUES ('Strive not to be a success, but rather to be of value.', 'Albert Einstein');
INSERT INTO quotes(quote, author) VALUES ('I attribute my success to this: I never gave or took any excuse.', 'Florence Nightingale');
INSERT INTO quotes(quote, author) VALUES ('You miss 100% of the shots you don''t take.', 'Wayne Gretzky');
INSERT INTO quotes(quote, author) VALUES ('The most difficult thing is the decision to act, the rest is merely tenacity.', 'Amelia Earhart');
INSERT INTO quotes(quote, author) VALUES ('We become what we think about.', 'Earl Nightingale');
INSERT INTO quotes(quote, author) VALUES ('The best time to plant a tree was 20 years ago. The second best time is now.', 'Chinese Proverb');
INSERT INTO quotes(quote, author) VALUES ('Eighty percent of success is showing up.', 'Woody Allen');
INSERT INTO quotes(quote, author) VALUES ('Winning isn''t everything, but wanting to win is.', 'Vince Lombardi');
INSERT INTO quotes(quote, author) VALUES ('Every child is an artist.  The problem is how to remain an artist once he grows up.', 'Pablo Picasso');
INSERT INTO quotes(quote, author) VALUES ('Success is liking yourself, liking what you do, and liking how you do it.', 'Maya Angelou');

INSERT INTO quotes(quote, author) VALUES ('Either you run the day, or the day runs you.', 'Jim Rohn');
INSERT INTO quotes(quote, author) VALUES ('Whether you think you can or you think you can''t, you''re right.', 'Henry Ford');
INSERT INTO quotes(quote, author) VALUES ('The two most important days in your life are the day you are born and the day you find out why.', 'Mark Twain');
INSERT INTO quotes(quote, author) VALUES ('Life shrinks or expands in proportion to one''s courage.', 'Anais Nin');
INSERT INTO quotes(quote, author) VALUES ('There is only one way to avoid criticism: do nothing, say nothing, and be nothing.', 'Aristotle');
INSERT INTO quotes(quote, author) VALUES ('Believe you can and you''re halfway there.', 'Theodore Roosevelt');
INSERT INTO quotes(quote, author) VALUES ('We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light.', 'Plato');
INSERT INTO quotes(quote, author) VALUES ('Success is walking from failure to failure with no loss of enthusiasm.', 'Winston Churchill');
INSERT INTO quotes(quote, author) VALUES ('Life is not measured by the number of breaths we take, but by the moments that take our breath away.', 'Maya Angelou');
INSERT INTO quotes(quote, author) VALUES ('Never make someone a priority when all you are to them is an option.', 'Maya Angelou');

INSERT INTO quotes(quote, author) VALUES ('We must believe that we are gifted for something, and that this thing, at whatever cost, must be attained.', 'Marie Curie');
INSERT INTO quotes(quote, author) VALUES ('I didn''t fail the test. I just found 100 ways to do it wrong.', 'Benjamin Franklin');
INSERT INTO quotes(quote, author) VALUES ('A person who never made a mistake never tried anything new.', 'Albert Einstein');
INSERT INTO quotes(quote, author) VALUES ('You become what you believe.', 'Oprah Winfrey');
INSERT INTO quotes(quote, author) VALUES ('I would rather die of passion than of boredom.', 'Vincent van Gogh');
INSERT INTO quotes(quote, author) VALUES ('If you want your children to turn out well, spend twice as much time with them, and half as much money.', 'Abigail Van Buren');
INSERT INTO quotes(quote, author) VALUES ('Opportunities don''t happen, you create them.', 'Chris Grosser');
INSERT INTO quotes(quote, author) VALUES ('You don''t get older, you get better', 'Shirley Bassey');
INSERT INTO quotes(quote, author) VALUES ('Dream big and dare to fail.', 'Norman Vaughan');
INSERT INTO quotes(quote, author) VALUES ('The distance between insanity and genius is measured only by success.', 'Bruce Feirstein');

INSERT INTO quotes(quote, author) VALUES ('Remember no one can make you feel inferior without your consent.', 'Eleanor Roosevelt');
INSERT INTO quotes(quote, author) VALUES ('The question isn''t who is going to let me; it''s who is going to stop me.', 'Ayn Rand');
INSERT INTO quotes(quote, author) VALUES ('When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.', 'Henry Ford');
INSERT INTO quotes(quote, author) VALUES ('It''s not the years in your life that count. It''s the life in your years.', 'Abraham Lincoln');
INSERT INTO quotes(quote, author) VALUES ('Either write something worth reading or do something worth writing.', 'Benjamin Franklin');
INSERT INTO quotes(quote, author) VALUES ('The only way to do great work is to love what you do.', 'Steve Jobs');
INSERT INTO quotes(quote, author) VALUES ('Moral indignation is jealousy with a halo.', 'H. G. Wells');
INSERT INTO quotes(quote, author) VALUES ('Glory is fleeting, but obscurity is forever.', 'Napoleon Bonaparte'); 
INSERT INTO quotes(quote, author) VALUES ('The whole problem with the world is that fools and fanatics are always so certain of themselves, and wiser people so full of doubts.', 'Bertrand Russell');
INSERT INTO quotes(quote, author) VALUES ('Don''t be so humble - you are not that great.', 'Golda Meier');
INSERT INTO quotes(quote, author) VALUES ('If a man does his best, what else is there?', 'George Patton');

INSERT INTO quotes(quote, author) VALUES ('Political correctness is tyranny with manners.', 'Charlton Heston');
INSERT INTO quotes(quote, author) VALUES ('You can avoid reality, but you cannot avoid the consequences of avoiding reality.', 'Ayn Rand');
INSERT INTO quotes(quote, author) VALUES ('Sex and religion are closer to each other than either might prefer.','Saint Thomas More');
INSERT INTO quotes(quote, author) VALUES ('People demand freedom of speech to make up for the freedom of thought which they avoid.','Soren Kierkegaard');
INSERT INTO quotes(quote, author) VALUES ('Not everything that can be counted counts, and not everything that counts can be counted.', 'Albert Einstein');
INSERT INTO quotes(quote, author) VALUES ('Only two things are infinite, the universe and human stupidity, and I''m not sure about the former.', 'Albert Einstein');
INSERT INTO quotes(quote, author) VALUES ('This book fills a much-needed gap.', 'Moses Hadas');
INSERT INTO quotes(quote, author) VALUES ('Give me a museum and I''ll fill it.', 'Pablo Picasso');
INSERT INTO quotes(quote, author) VALUES ('In theory, there is no difference between theory and practice. But in practice, there is.', 'Yogi Berra');
INSERT INTO quotes(quote, author) VALUES ('I find that the harder I work, the more luck I seem to have.', 'Thomas Jefferson');

INSERT INTO quotes(quote, author) VALUES ('The only way to get rid of a temptation is to yield to it.', 'Oscar Wilde');
INSERT INTO quotes(quote, author) VALUES ('There are no facts, only interpretations.', 'Friedrich Nietzsche');
INSERT INTO quotes(quote, author) VALUES ('A mathematician is a device for turning coffee into theorems.', 'Paul Erdos');
INSERT INTO quotes(quote, author) VALUES ('Try to learn something about everything and everything about something.', 'Thomas Henry Huxley');
INSERT INTO quotes(quote, author) VALUES ('The only difference between me and a madman is that I''m not mad.', 'Salvador Dali'); 
INSERT INTO quotes(quote, author) VALUES ('We have art to save ourselves from the truth.', 'Friedrich Nietzsche');
INSERT INTO quotes(quote, author) VALUES ('I have never killed anyone, but I have read some obituary notices with great satisfaction.', 'Clarence Darrow');
INSERT INTO quotes(quote, author) VALUES ('I have nothing to declare except my genius.', 'Oscar Wilde'); 
INSERT INTO quotes(quote, author) VALUES ('Talent does what it can; genius does what it must.', 'Edward George Bulwer-Lytton');
INSERT INTO quotes(quote, author) VALUES ('Women might be able to fake orgasms. But men can fake a whole relationship.', 'Sharon Stone');

INSERT INTO quotes(quote, author) VALUES ('Many wealthy people are little more than janitors of their possessions.', 'Frank Lloyd Wright'); 
INSERT INTO quotes(quote, author) VALUES ('He is one of those people who would be enormously improved by death.', 'H. H. Munro'); 
INSERT INTO quotes(quote, author) VALUES ('I shall not waste my days in trying to prolong them.', 'Ian L. Fleming');
INSERT INTO quotes(quote, author) VALUES ('If you can count your money, you don''t have a billion dollars.', 'J. Paul Getty');
INSERT INTO quotes(quote, author) VALUES ('Facts are the enemy of truth.', 'Don Quixote');
INSERT INTO quotes(quote, author) VALUES ('Maybe this world is another planet''s Hell.', 'Aldous Huxley');
INSERT INTO quotes(quote, author) VALUES ('It''s kind of fun to do the impossible.', 'Walt Disney');
INSERT INTO quotes(quote, author) VALUES ('We didn''t lose the game; we just ran out of time.', 'Vince Lombardi');
INSERT INTO quotes(quote, author) VALUES ('The optimist proclaims that we live in the best of all possible worlds, and the pessimist fears this is true.', 'James Branch Cabell');
INSERT INTO quotes(quote, author) VALUES ('All are lunatics, but he who can analyze his delusion is called a philosopher.', 'Ambrose Bierce');

INSERT INTO quotes(quote, author) VALUES ('The true measure of a man is how he treats someone who can do him absolutely no good.', 'Samuel Johnson');
INSERT INTO quotes(quote, author) VALUES ('There is more stupidity than hydrogen in the universe, and it has a longer shelf life.', 'Frank Zappa');
INSERT INTO quotes(quote, author) VALUES ('Life is pleasant. Death is peaceful. It''s the transition that''s troublesome.', 'Isaac Asimov');
INSERT INTO quotes(quote, author) VALUES ('If you want to make an apple pie from scratch, you must first create the universe.', 'Carl Sagan');
INSERT INTO quotes(quote, author) VALUES ('Knowledge speaks, but wisdom listens.', 'Jimi Hendrix');
INSERT INTO quotes(quote, author) VALUES ('A clever man commits no minor blunders.', 'Goethe');
INSERT INTO quotes(quote, author) VALUES ('A witty saying proves nothing.', 'Voltaire');
INSERT INTO quotes(quote, author) VALUES ('The nice thing about being a celebrity is that if you bore people they think it''s their fault.', 'Henry Kissinger');
INSERT INTO quotes(quote, author) VALUES ('If everything seems under control, you''re just not going fast enough.', 'Mario Andretti');
INSERT INTO quotes(quote, author) VALUES ('I''ll sleep when I''m dead.', 'Warren Zevon');

INSERT INTO quotes(quote, author) VALUES ('While we are postponing, life speeds by.', 'Seneca');
INSERT INTO quotes(quote, author) VALUES ('First they ignore you, then they laugh at you, then they fight you, then you win.', 'Mahatma Gandhi');
INSERT INTO quotes(quote, author) VALUES ('Tragedy is when I cut my finger. Comedy is when you walk into an open sewer and die.', 'Mel Brooks');
INSERT INTO quotes(quote, author) VALUES ('A narcissist is someone better looking than you are.', 'Gore Vidal');
INSERT INTO quotes(quote, author) VALUES ('Wise men make proverbs, but fools repeat them.', 'Samuel Palmer'); 
INSERT INTO quotes(quote, author) VALUES ('The secret of success is to know something nobody else knows.', 'Aristotle Onassis');
INSERT INTO quotes(quote, author) VALUES ('Sometimes when reading Goethe I have the paralyzing suspicion that he is trying to be funny.', 'Guy Davenport');
INSERT INTO quotes(quote, author) VALUES ('When you have to kill a man, it costs nothing to be polite.', 'Winston Churchill'); 
INSERT INTO quotes(quote, author) VALUES ('Any man who is under 30, and is not a liberal, has no heart; and any man who is over 30, and is not a conservative, has no brains.', 'Sir Winston Churchill'); 
INSERT INTO quotes(quote, author) VALUES ('We all agree that your theory is crazy, but is it crazy enough?', 'Niels Bohr'); 

INSERT INTO quotes(quote, author) VALUES ('I would have made a good Pope.', 'Richard Nixon');
INSERT INTO quotes(quote, author) VALUES ('Reality is merely an illusion, albeit a very persistent one.', 'Albert Einstein');
INSERT INTO quotes(quote, author) VALUES ('One of the symptoms of an approaching nervous breakdown is the belief that one''s work is terribly important.', 'Bertrand Russell');
INSERT INTO quotes(quote, author) VALUES ('Make everything as simple as possible, but not simpler.', 'Albert Einstein');
INSERT INTO quotes(quote, author) VALUES ('It is dangerous to be sincere unless you are also stupid.', 'George Bernard Shaw');
INSERT INTO quotes(quote, author) VALUES ('A man can''t be too careful in the choice of his enemies.', 'Oscar Wilde');
INSERT INTO quotes(quote, author) VALUES ('Forgive your enemies, but never forget their names.', 'John F. Kennedy'); 
INSERT INTO quotes(quote, author) VALUES ('No one can earn a million dollars honestly.', 'William Jennings Bryan');
INSERT INTO quotes(quote, author) VALUES ('When ideas fail, words come in very handy.', 'Goethe');
INSERT INTO quotes(quote, author) VALUES ('In the end, everything is a gag.', 'Charlie Chaplin'); 

INSERT INTO quotes(quote, author) VALUES ('I love Mickey Mouse more than any woman I have ever known.', 'Walt Disney');
INSERT INTO quotes(quote, author) VALUES ('He who hesitates is a damned fool.', 'Mae West');
INSERT INTO quotes(quote, author) VALUES ('University politics are vicious precisely because the stakes are so small.', 'Henry Kissinger');
INSERT INTO quotes(quote, author) VALUES ('The graveyards are full of indispensable men.', 'Charles de Gaulle');
INSERT INTO quotes(quote, author) VALUES ('Behind every great fortune there is a crime.', 'Honore de Balzac');
INSERT INTO quotes(quote, author) VALUES ('I am not young enough to know everything.','Oscar Wilde' );
INSERT INTO quotes(quote, author) VALUES ('Bigamy is having one wife too many. Monogamy is the same.', 'Oscar Wilde' ); 
INSERT INTO quotes(quote, author) VALUES ('The object of war is not to die for your country but to make the other bastard die for his.', 'George Patton');
INSERT INTO quotes(quote, author) VALUES ('Sometimes a scream is better than a thesis.', 'Ralph Waldo Emerson');
INSERT INTO quotes(quote, author) VALUES ('The covers of this book are too far apart.', 'Ambrose Bierce'); 

INSERT INTO quotes(quote, author) VALUES ('Anything that is too stupid to be spoken is sung.', 'Voltaire');
INSERT INTO quotes(quote, author) VALUES ('No Sane man will dance.', 'Cicero');
INSERT INTO quotes(quote, author) VALUES ('Hell is other people.', 'Jean-Paul Sartre' );
INSERT INTO quotes(quote, author) VALUES ('Friends may come and go, but enemies accumulate.', 'Thomas Jones');
INSERT INTO quotes(quote, author) VALUES ('The gods too are fond of a joke.', 'Aristotle');
INSERT INTO quotes(quote, author) VALUES ('The cynics are right nine times out of ten.', 'Henry Louis Mencken' );
INSERT INTO quotes(quote, author) VALUES ('Attention to health is life''s greatest hindrance.', 'Plato' ); 
INSERT INTO quotes(quote, author) VALUES ('Plato was a bore.', 'Friedrich Nietzsche');
INSERT INTO quotes(quote, author) VALUES ('Nietzsche was stupid and abnormal.', 'Leo Tolstoy');
INSERT INTO quotes(quote, author) VALUES ('I''m not going to get into the ring with Tolstoy.', 'Ernest Hemingway');

INSERT INTO quotes(quote, author) VALUES ('Men have become the tools of their tools.', 'Henry David Thoreau');
INSERT INTO quotes(quote, author) VALUES ('I have never let my schooling interfere with my education.', 'Mark Twain' );
INSERT INTO quotes(quote, author) VALUES ('Sanity is a madness put to good uses.', 'George Santayana');
INSERT INTO quotes(quote, author) VALUES ('In America, anybody can be president. That''s one of the risks you take.', 'Adlai Stevenson');
INSERT INTO quotes(quote, author) VALUES ('Some editors are failed writers, but so are most writers.', 'T. S. Eliot');
INSERT INTO quotes(quote, author) VALUES ('It is better to be quotable than to be honest.', 'Tom Stoppard' );
INSERT INTO quotes(quote, author) VALUES ('Never mistake motion for action.', 'Ernest Hemingway'  ); 
INSERT INTO quotes(quote, author) VALUES ('Learning is what most adults will do for a living in the 21st century.', 'Lewis Perelman');
INSERT INTO quotes(quote, author) VALUES ('A pessimist sees the difficulty in every opportunity; an optimist sees the opportunity in every difficulty.', 'Winston Churchill');
INSERT INTO quotes(quote, author) VALUES ('Speak softly, and carry a big stick.', 'Theodore Roosevelt');

INSERT INTO quotes(quote, author) VALUES ('I think there is a world market for maybe five computers.', 'Thomas Watson'); 
INSERT INTO quotes(quote, author) VALUES ('The only thing necessary for the triumph of evil is for good men to do nothing.', 'Edmund Burke');
INSERT INTO quotes(quote, author) VALUES ('There is no reason anyone would want a computer in their home.', 'Ken Olson' );
INSERT INTO quotes(quote, author) VALUES ('Everything that can be invented has been invented.', 'Charles H. Duell');
INSERT INTO quotes(quote, author) VALUES ('The difference between fiction and reality? Fiction has to make sense.', 'Tom Clancy');
INSERT INTO quotes(quote, author) VALUES ('Whatever is begun in anger ends in shame.', 'Benjamin Franklin' );
INSERT INTO quotes(quote, author) VALUES ('There''s many a bestseller that could have been prevented by a good teacher.', 'Flannery O''Connor' );
INSERT INTO quotes(quote, author) VALUES ('Write drunk; edit sober.', 'Ernest Hemingway'); 
INSERT INTO quotes(quote, author) VALUES ('He would make a lovely corpse.', 'Charles Dickens');
INSERT INTO quotes(quote, author) VALUES ('Wagner''s music is better than it sounds.', 'Mark Twain');
INSERT INTO quotes(quote, author) VALUES ('If you were plowing a field, which would you rather use? Two strong oxen or 1024 chickens?', 'Seymour Cray'); 

INSERT INTO quotes(quote, author) VALUES ('The man who does not read good books has no advantage over the man who cannot read them.', 'Mark Twain');
INSERT INTO quotes(quote, author) VALUES ('The truth is more important than the facts.', 'Frank Lloyd Wright' );
INSERT INTO quotes(quote, author) VALUES ('I''m not afraid of death; I just don''t want to be there when it happens.', 'Woody Allen' );
INSERT INTO quotes(quote, author) VALUES ('All the world is made of faith, and trust, and pixie dust.', 'Peter Pan');
INSERT INTO quotes(quote, author) VALUES ('I don''t know the question, but sex is definitely the answer.', 'Woody Allen');
INSERT INTO quotes(quote, author) VALUES ('It is said that your life flashes before your eyes just before you die. That is true, it''s called Life.', 'Terry Pratchett' );
INSERT INTO quotes(quote, author) VALUES ('Two possibilities exist: either we are alone in the Universe or we are not. Both are equally terrifying.', 'Arthur C. Clarke' );
INSERT INTO quotes(quote, author) VALUES ('Appear weak when you are strong, and strong when you are weak.', 'Sun Tzu'); 
INSERT INTO quotes(quote, author) VALUES ('You live but once; you might as well be amusing.', 'Coco Chanel');
INSERT INTO quotes(quote, author) VALUES ('It''s better to burn out than to fade away.', 'Neil Young');
INSERT INTO quotes(quote, author) VALUES ('The fool doth think he is wise, but the wise man knows himself to be a fool.', 'William Shakespeare');

INSERT INTO quotes(quote, author) VALUES ('It ain''t over till the fat lady sings', 'Sports colloquialism' );
INSERT INTO quotes(quote, author) VALUES ('The saddest aspect of life right now is that science gathers knowledge faster than society gathers wisdom.', 'Isaac Asimov' );
INSERT INTO quotes(quote, author) VALUES ('Turn your wounds into wisdom.', 'Oprah Winfrey' );
INSERT INTO quotes(quote, author) VALUES ('Any fool can know. The point is to understand.', 'Albert Einstein');
INSERT INTO quotes(quote, author) VALUES ('The only man who never makes mistakes is the man who never does anything.', 'Theodore Roosevelt');
INSERT INTO quotes(quote, author) VALUES ('It takes a very long time to become young.', 'Pablo Picasso' );
INSERT INTO quotes(quote, author) VALUES ('Prediction is very difficult, especially about the future.', 'Niels Bohr' );
INSERT INTO quotes(quote, author) VALUES ('Healthy citizens are the greatest asset any country can have.', 'Winston Churchill');
INSERT INTO quotes(quote, author) VALUES ('He must be very ignorant for he answers every question he is asked.', 'Voltaire');
INSERT INTO quotes(quote, author) VALUES ('It takes a lot of rehearsing for a man to be himself.', 'William Saroyan'); 

INSERT INTO quotes(quote, author) VALUES ('A clear vision, backed by definite plans, gives you a tremendous feeling of confidence and personal power.', 'Brian Tracy');
INSERT INTO quotes(quote, author) VALUES ('The revolution is not an apple that falls when ripe. You have to make it fall.', 'Che Guevara' );
INSERT INTO quotes(quote, author) VALUES ('Fashion and music are the same, because music express its period too.', 'Karl Lagerfeld' );
INSERT INTO quotes(quote, author) VALUES ('Never say anything about yourself you don''t want to come true.', 'Brian Tracy');
INSERT INTO quotes(quote, author) VALUES ('If you tell the truth, you don''t have to remember anything.', 'Mark Twain');
INSERT INTO quotes(quote, author) VALUES ('In a time of deceit telling the truth is a revolutionary act.', 'George Orwell' );
INSERT INTO quotes(quote, author) VALUES ('Art is the lie that enables us to realize the truth.', 'Pablo Picasso' );
INSERT INTO quotes(quote, author) VALUES ('If the road is easy, you''re likely going the wrong way.', 'Terry Goodkind'); 
INSERT INTO quotes(quote, author) VALUES ('Like all dreamers I confuse disenchantment with truth.', 'Jean-Paul Sartre');
INSERT INTO quotes(quote, author) VALUES ('If I have seen further it is by standing on the shoulders of Giants.', 'Isaac Newton');

INSERT INTO quotes(quote, author) VALUES ('If you wish to make an apple pie from scratch, you must first invent the universe.', 'Carl Sagan'); 
INSERT INTO quotes(quote, author) VALUES ('Life would be tragic if it weren''t funny.', 'Stephen Hawking');
INSERT INTO quotes(quote, author) VALUES ('We are all star stuff.', 'Carl Sagan' );
INSERT INTO quotes(quote, author) VALUES ('A friend is someone who knows all about you and still loves you.', 'Elbert Hubbard' );
INSERT INTO quotes(quote, author) VALUES ('It is not a lack of love, but a lack of friendship that makes unhappy marriages.', 'Friedrich Nietzsche');
INSERT INTO quotes(quote, author) VALUES ('It is hard to fail, but it is worse never to have tried to succeed.', 'Theodore Roosevelt');
INSERT INTO quotes(quote, author) VALUES ('90% of the work in this country is done by people who don''t feel good.', 'Theodore Roosevelt' );
INSERT INTO quotes(quote, author) VALUES ('The first step toward success is taken when you refuse to be a captive of the environment in which you first find yourself.', 'Mark Claine');
INSERT INTO quotes(quote, author) VALUES ('When I dare to be powerful – to use my strength in the service of my vision, then it becomes less and less important whether I am afraid.', 'Audre Lorde');
INSERT INTO quotes(quote, author) VALUES ('Whenever you find yourself on the side of the majority, it is time to pause and reflect.', 'Mark Twain' );

INSERT INTO quotes(quote, author) VALUES ('Great minds discuss ideas; average minds discuss events; small minds discuss people.', 'Eleanor Roosevelt'); 
INSERT INTO quotes(quote, author) VALUES ('A successful man is one who can lay a firm foundation with the bricks others have thrown at him.', 'David Brinkley');
INSERT INTO quotes(quote, author) VALUES ('Live as if you were to die tomorrow. Learn as if you were to live forever.', 'Mahatma Gandhi' );
INSERT INTO quotes(quote, author) VALUES ('Twenty years from now you will be more disappointed by the things that you didn''t do than by the ones you did do.', 'Mark Twain' );
INSERT INTO quotes(quote, author) VALUES ('The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack of will.', 'Vince Lombardi');
INSERT INTO quotes(quote, author) VALUES ('It is our choices, that show what we truly are, far more than our abilities.', 'J. K Rowling');
INSERT INTO quotes(quote, author) VALUES ('You have to learn the rules of the game. And then you have to play better than anyone else.', 'Albert Einstein' );
INSERT INTO quotes(quote, author) VALUES ('The successful warrior is the average man, with laser-like focus.', 'Bruce Lee');
INSERT INTO quotes(quote, author) VALUES ('Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.', 'Dale Carnegie');
INSERT INTO quotes(quote, author) VALUES ('If you genuinely want something, don''t wait for it – teach yourself to be impatient.', 'Gurbaksh Chanal' );

INSERT INTO quotes(quote, author) VALUES ('Don''t let the fear of losing be greater than the excitement of winning.', 'Robert Kiyosaki'); 
INSERT INTO quotes(quote, author) VALUES ('I cannot live without books.', 'Thomas Jefferson');
INSERT INTO quotes(quote, author) VALUES ('The books that the world calls immoral are the books that show the world its own shame.', 'Oscar Wilde' );
INSERT INTO quotes(quote, author) VALUES ('There is creative reading as well as creative writing.', 'Ralph Waldo Emerson' );
INSERT INTO quotes(quote, author) VALUES ('Next to acquiring good friends, the best acquisition is that of good books.', 'Charles Caleb Colton');
INSERT INTO quotes(quote, author) VALUES ('I would sooner read a timetable or a catalog than nothing at all.', 'W. Somerset Maugham');
INSERT INTO quotes(quote, author) VALUES ('The journey of a thousand miles must begin with a single step.', 'Chinese proverb' );
INSERT INTO quotes(quote, author) VALUES ('Who has never tasted what is bitter does not know what is sweet.', 'German proverb');
INSERT INTO quotes(quote, author) VALUES ('A truth spoken before its time is dangerous.', 'Greek proverb');
INSERT INTO quotes(quote, author) VALUES ('A hero is a man who is afraid to run away.', 'English proverb' );

INSERT INTO quotes(quote, author) VALUES ('Mathematics may be defined as the subject in which we never know what we are talking about, nor whether what we are saying is true.', 'Bertrand Russel'); 
INSERT INTO quotes(quote, author) VALUES ('Men are only as good as their technical development allows them to be.', 'George Orwell');
INSERT INTO quotes(quote, author) VALUES ('Man is still the most extraordinary computer of all.', 'John F. Kennedy' );
INSERT INTO quotes(quote, author) VALUES ('Computers are useless. They can only give you answers.', 'Pablo Picasso' );
INSERT INTO quotes(quote, author) VALUES ('You never know how much you really believe anything until its truth or falsehood becomes a matter of life and death to you.', 'C.S. Lewis');
INSERT INTO quotes(quote, author) VALUES ('To have no time for philosophy is to be a true philosopher.', 'Blaise Pascal');
INSERT INTO quotes(quote, author) VALUES ('Those who lack the courage will always find a philosophy to justify it.', 'Albert Camus' );
INSERT INTO quotes(quote, author) VALUES ('The philosopher proves that the philosopher exists. The poet merely enjoys existence.', 'Wallace Stevens');
INSERT INTO quotes(quote, author) VALUES ('Philosophy is the product of wonder.', 'Alfred North Whitehead');
INSERT INTO quotes(quote, author) VALUES ('The family is one of nature''s masterpieces.', 'George Santayana' );

INSERT INTO quotes(quote, author) VALUES ('Diaper backward spells repaid. Think about it.', 'Marshall Mcluhan' );
INSERT INTO quotes(quote, author) VALUES ('It is a wise father that knows his own child.', 'William Shakespeare');
INSERT INTO quotes(quote, author) VALUES ('There are fathers who do not love their children, but there is no grandfather who does not adore his grandson.', 'Victor Hugo');
INSERT INTO quotes(quote, author) VALUES ('The family spirit has rendered man carnivorous.', 'Francis Picabia' );
INSERT INTO quotes(quote, author) VALUES ('Cruel is the strife of brothers.', 'Aristotle');
INSERT INTO quotes(quote, author) VALUES ('All that live must die, passing through nature to eternity.', 'William Shakespeare');
INSERT INTO quotes(quote, author) VALUES ('Every man must do two things alone; he must do his own believing and his own dying.', 'Martin Luther' );
INSERT INTO quotes(quote, author) VALUES ('Don''t be afraid to give up the good to go for the great.', 'John D. Rockefeller');
INSERT INTO quotes(quote, author) VALUES ('Innovation distinguishes between a leader and a follower.', 'Steve Jobs');
INSERT INTO quotes(quote, author) VALUES ('All progress takes place outside the comfort zone.', 'Michael John Bobak' );

INSERT INTO quotes(quote, author) VALUES ('All animals are equal, but some animals are more equal than others.', 'George Orwell'); 
INSERT INTO quotes(quote, author) VALUES ('Words are, of course, the most powerful drug used by mankind.', 'Rudyard Kipling');
INSERT INTO quotes(quote, author) VALUES ('All words are pegs to hang ideas on.', 'Henry Ward Beecher' );
INSERT INTO quotes(quote, author) VALUES ('For last year''s words belong to last year''s language and next year''s words await another voice.', 'T.S. Elliot' );
INSERT INTO quotes(quote, author) VALUES ('The right word may be effective, but no word was ever as effective as a rightly timed pause.', 'Mark Twain');
INSERT INTO quotes(quote, author) VALUES ('The last thing a political party gives up is its vocabulary.', 'Alexis de Tocqueville');
INSERT INTO quotes(quote, author) VALUES ('Words are loaded pistols.', 'Jean-Paul Sartre' );
INSERT INTO quotes(quote, author) VALUES ('If you can dream it, you can do it. Always remember this whole thing was started by a mouse.', 'Walt Disney');
INSERT INTO quotes(quote, author) VALUES ('We grow great by dreams. All big men are dreamers.', 'Woodrow Wilson');
INSERT INTO quotes(quote, author) VALUES ('I''ve never been an intellectual but I have this look.', 'Woody Allen' );

INSERT INTO quotes(quote, author) VALUES ('My name is Sherlock Holmes. It is my business to know what other people don''t know.', 'Sherlock Holmes' );
INSERT INTO quotes(quote, author) VALUES ('Eliminate all other factors, and the one which remains must be the truth.', 'Sherlock Holmes' );
INSERT INTO quotes(quote, author) VALUES ('Music expresses that which cannot be put into words and that which cannot remain silent.', 'Victor Hugo' );
INSERT INTO quotes(quote, author) VALUES ('Literature is a luxury; fiction is a necessity.', 'G.K. Chesterton' );
INSERT INTO quotes(quote, author) VALUES ('Without literature, life is hell.', 'Charles Bukowski' );
INSERT INTO quotes(quote, author) VALUES ('The man who reads nothing at all is better educated than the man who reads nothing but newspapers.', 'Thomas Jefferson' );
INSERT INTO quotes(quote, author) VALUES ('Keep your friends close, but your enemies closer.', 'Sun Tzu' );
INSERT INTO quotes(quote, author) VALUES ('We look forward to the time when the Power of Love will replace the Love of Power. Then will our world know the blessings of peace.', 'William Ewart Gladstone' );
INSERT INTO quotes(quote, author) VALUES ('It is better to remain silent at the risk of being thought a fool, than to talk and remove all doubt of it.', 'Maurice Switzer' );
INSERT INTO quotes(quote, author) VALUES ('If opportunity doesn''t knock, build a door.', 'Milton Berle' );

INSERT INTO quotes(quote, author) VALUES ('Everything in moderation, including moderation.', 'Oscar Wilde' );
INSERT INTO quotes(quote, author) VALUES ('The trouble with eating Italian food is that five or six days later, you''re hungry again.', 'George Miller' );
INSERT INTO quotes(quote, author) VALUES ('Always borrow money from a pessimist. He won''t expect it back.', 'Oscar Wilde' );
INSERT INTO quotes(quote, author) VALUES ('Courage is contagious. When a brave man takes a stand, the spines of others are stiffened.', 'Billy Graham' );
INSERT INTO quotes(quote, author) VALUES ('Patience is something you admire in the driver behind you, but not in one ahead.', 'Bill McGlashen' );
INSERT INTO quotes(quote, author) VALUES ('It is the mark of an educated mind to be able to entertain a thought without accepting it.', 'Aristotle' );
INSERT INTO quotes(quote, author) VALUES ('Waiting for perfect is never as smart as making progress.', 'Seth Godin' );
INSERT INTO quotes(quote, author) VALUES ('I have never in my life learned anything from any man who agreed with me.', 'Dudley Field Malone' );
INSERT INTO quotes(quote, author) VALUES ('Little minds are tamed and subdued by misfortune; but great minds rise above them.', 'Washington Irving' );
INSERT INTO quotes(quote, author) VALUES ('People who read the tabloids deserve to be lied to.', 'Jerry Seinfeld' );

INSERT INTO quotes(quote, author) VALUES ('No man is rich enough to buy back his past.', 'Oscar Wilde' );
INSERT INTO quotes(quote, author) VALUES ('To the world you may be just one person, but to one person you may be the world.', 'Brandi Snyder' );
INSERT INTO quotes(quote, author) VALUES ('It''s useless to hold a person to anything he says while he''s in love, drunk, or running for office.', 'Shirley MacLaine' );
INSERT INTO quotes(quote, author) VALUES ('Never tell your problems to anyone... 20% don''t care and the other 80% are glad you have them.', 'Lou Holtz' );
INSERT INTO quotes(quote, author) VALUES ('There''s zero correlation between being the best talker and having the best ideas.', 'Susan Cain' );
INSERT INTO quotes(quote, author) VALUES ('Failure is the condiment that gives success its flavor.', 'Truman Capote' );
INSERT INTO quotes(quote, author) VALUES ('In dreams and in love there are no impossibilities.', 'Janos Arany' );
INSERT INTO quotes(quote, author) VALUES ('He, who will not reason, is a bigot; he, who cannot, is a fool; and he, who dares not, is a slave.', 'William Drummond' );
INSERT INTO quotes(quote, author) VALUES ('If you have knowledge, let others light their candles in it.', 'Margaret Fuller' );
INSERT INTO quotes(quote, author) VALUES ('The best way to predict the future is to invent it.', 'Alan Kay' );

INSERT INTO quotes(quote, author) VALUES ('Remember that happiness is a way of travel, not a destination.', 'Roy Goodman' );
INSERT INTO quotes(quote, author) VALUES ('The only thing worse than being blind is having sight but no vision.', 'Helen Keller' );
INSERT INTO quotes(quote, author) VALUES ('Always forgive your enemies; nothing annoys them so much.', 'Oscar Wilde' );
INSERT INTO quotes(quote, author) VALUES ('It is easier to judge the mind of a man by his questions rather than his answers.', 'Pierre-Marc-Gaston De Levis' );
INSERT INTO quotes(quote, author) VALUES ('Love all, trust a few, do wrong to none.', 'William Shakespeare' );
INSERT INTO quotes(quote, author) VALUES ('Don''t look for big things, just do small things with great love.', 'Mother Teresa' );
INSERT INTO quotes(quote, author) VALUES ('Without music, life would be a mistake.', 'Friedrich Nietzsche' );
INSERT INTO quotes(quote, author) VALUES ('You must be the change that you wish to see in the world.', 'Mahatma Gandhi' );
INSERT INTO quotes(quote, author) VALUES ('You only live once, but if you do it right, once is enough.', 'Mae West' );
INSERT INTO quotes(quote, author) VALUES ('The cave you fear to enter holds the treasure you seek.', 'Joseph Campbell' );

INSERT INTO quotes(quote, author) VALUES ('If you don''t build your dream, someone else will hire you to help them build theirs.', 'Dhirubhai Ambani' );
INSERT INTO quotes(quote, author) VALUES ('Things come apart so easily when they have been held together with lies.', 'Dorothy Allison' );
INSERT INTO quotes(quote, author) VALUES ('Let him who would enjoy a good future waste none of his present.', 'Roger Babson' );
INSERT INTO quotes(quote, author) VALUES ('Don''t cry because it''s over, smile because it happened.', 'Dr. Seuss' );
INSERT INTO quotes(quote, author) VALUES ('To handle yourself, use your head; to handle others, use your heart.', 'Eleanor Roosevelt' );
INSERT INTO quotes(quote, author) VALUES ('Too many of us are not living our dreams because we are living our fears.', 'Les Brown' );
INSERT INTO quotes(quote, author) VALUES ('I am not a product of my circumstances. I am a product of my decisions.', 'Stephen Covey' );
INSERT INTO quotes(quote, author) VALUES ('The most common way people give up their power is by thinking they don''t have any. ', 'Alice Walker' );
INSERT INTO quotes(quote, author) VALUES ('It is during our darkest moments that we must focus to see the light.', 'Aristotle Onassis' );
INSERT INTO quotes(quote, author) VALUES ('You can''t use up creativity. The more you use, the more you have.', 'Maya Angelou' );

INSERT INTO quotes(quote, author) VALUES ('Love truth, but pardon error.', 'Voltaire' );
INSERT INTO quotes(quote, author) VALUES ('Certain things catch your eye, but pursue only those that capture the heart.', 'Ancient Indian Proverb' );
INSERT INTO quotes(quote, author) VALUES ('We can''t help everyone, but everyone can help someone.', 'Ronald Reagan' );
INSERT INTO quotes(quote, author) VALUES ('Everything you''ve ever wanted is on the other side of fear.', 'George Addair' );
INSERT INTO quotes(quote, author) VALUES ('What we achieve inwardly will change outer reality.', 'Plutarch' );
INSERT INTO quotes(quote, author) VALUES ('I believe in benevolent dictatorship, provided I am the dictator.', 'Richard Branson');
INSERT INTO quotes(quote, author) VALUES ('I wasn''t satisfied just to earn a good living. I was looking to make a statement.', 'Donald Trump' );
INSERT INTO quotes(quote, author) VALUES ('Do you want to know who you are? Don''t ask. Act! Action will delineate and define you.', 'Thomas Jefferson' );
INSERT INTO quotes(quote, author) VALUES ('Old minds are like old horses; you must exercise them if you wish to keep them in working order.', 'John Adams' );
INSERT INTO quotes(quote, author) VALUES ('It is better to be alone than in bad company.', 'George Washington' );

INSERT INTO quotes(quote, author) VALUES ('All I am, or can be, I owe to my angel mother.', 'Abraham Lincoln'); 
INSERT INTO quotes(quote, author) VALUES ('I find that when you have a real interest in life and a curious life, that sleep is not the most important thing.', 'Martha Stewart' );
INSERT INTO quotes(quote, author) VALUES ('The road to success and the road to failure are almost exactly the same.', 'Colin Davis' );
INSERT INTO quotes(quote, author) VALUES ('As we look ahead into the next century, leaders will be those who empower others.', 'Bill Gates' );
INSERT INTO quotes(quote, author) VALUES ('You must expect great things of yourself before you can do them.', 'Michael Jordan' );
INSERT INTO quotes(quote, author) VALUES ('You''ve got to get up every morning with determination if you''re going to go to bed with satisfaction.', 'George Lorimer');
INSERT INTO quotes(quote, author) VALUES ('Be miserable. Or motivate yourself. Whatever has to be done, it''s always your choice.', 'Wayne Dyer' );
INSERT INTO quotes(quote, author) VALUES ('Real difficulties can be overcome; it is only the imaginary ones that are unconquerable.', 'Theodore Vail' );
INSERT INTO quotes(quote, author) VALUES ('It is better to fail in originality than to succeed in imitation.', 'Herman Melville' );
INSERT INTO quotes(quote, author) VALUES ('Don''t let what you cannot do interfere with what you can do.', 'John Wooden' );

INSERT INTO quotes(quote, author) VALUES ('When you can measure what you are speaking about, and express it in numbers, you know something about it.', 'Lord Kelvin');
INSERT INTO quotes(quote, author) VALUES ('We are what we pretend to be, so we must be careful about what we pretend to be.', 'Kurt Vonnegut' );
INSERT INTO quotes(quote, author) VALUES ('You never have to change anything you got up in the middle of the night to write.', 'Saul Bellow' );
INSERT INTO quotes(quote, author) VALUES ('Pain is temporary. Quitting lasts forever.', 'Lance Armstrong' );
INSERT INTO quotes(quote, author) VALUES ('You have power over your mind - not outside events. Realize this, and you will find strength.', 'Marcus Aurelius' );
INSERT INTO quotes(quote, author) VALUES ('Romance is the glamour which turns the dust of everyday life into a golden haze.', 'Elinor Glyn');
INSERT INTO quotes(quote, author) VALUES ('It''s hard to beat a person who never gives up.', 'Babe Ruth' );
INSERT INTO quotes(quote, author) VALUES ('The soul is healed by being with children.', 'Fyodor Dostoyevsky' );
INSERT INTO quotes(quote, author) VALUES ('All the effort in the world won''t matter if you''re not inspired.', 'Chuck Palahniuk' );
INSERT INTO quotes(quote, author) VALUES ('Our wounds are often the openings into the best and most beautiful part of us.', 'David Richo' );

INSERT INTO quotes(quote, author) VALUES ('The reason I talk to myself is because I''m the only one whose answers I accept.', 'George Carlin');
INSERT INTO quotes(quote, author) VALUES ('The truth is rarely pure and never simple.', 'Oscar Wilde' );
INSERT INTO quotes(quote, author) VALUES ('The truth will set you free, but first it will piss you off.', 'Gloria Steinem' );
INSERT INTO quotes(quote, author) VALUES ('Rather than love, than money, than fame, give me truth.', 'Henry David Thoreau' );
INSERT INTO quotes(quote, author) VALUES ('The best way to find out if you can trust somebody is to trust them.', 'Ernest Hemingway' );
INSERT INTO quotes(quote, author) VALUES ('There are three types of lies -- lies, damn lies, and statistics.', 'Benjamin Disraeli');
INSERT INTO quotes(quote, author) VALUES ('No persons are more frequently wrong, than those who will not admit they are wrong.', 'Francois de La Rochefoucauld' );
INSERT INTO quotes(quote, author) VALUES ('The past has no power over the present moment.', 'Eckhart Tolle' );
INSERT INTO quotes(quote, author) VALUES ('The truth isn''t always beauty, but the hunger for it is.', 'Nadine Gordimer' );
INSERT INTO quotes(quote, author) VALUES ('Perhaps the truth depends on a walk around the lake.', 'Wallace Stevens' );

INSERT INTO quotes(quote, author) VALUES ('Be who you are and say what you feel, because those who mind don''t matter, and those who matter don''t mind.', 'Bernard Baruch');
INSERT INTO quotes(quote, author) VALUES ('You know you''re in love when you can''t fall asleep because reality is finally better than your dreams.', 'Dr. Seuss' );
INSERT INTO quotes(quote, author) VALUES ('Don''t walk behind me; I may not lead. Don''t walk in front of me; I may not follow. Just walk beside me and be my friend.', 'Albert Camus' );
INSERT INTO quotes(quote, author) VALUES ('Darkness cannot drive out darkness: only light can do that. Hate cannot drive out hate: only love can do that.', 'Martin Luther King Jr.' );
INSERT INTO quotes(quote, author) VALUES ('To live is the rarest thing in the world. Most people exist, that is all.', 'Oscar Wilde' );
INSERT INTO quotes(quote, author) VALUES ('Insanity is doing the same thing, over and over again, but expecting different results.', 'Albert Einstein');
INSERT INTO quotes(quote, author) VALUES ('It is better to be hated for what you are than to be loved for what you are not.', 'Andre Gide' );
INSERT INTO quotes(quote, author) VALUES ('The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.', 'Jane Austen' );
INSERT INTO quotes(quote, author) VALUES ('The fool doesn''t think he is wise, but the wise man knows himself to be a fool.', 'William Shakespeare' );
INSERT INTO quotes(quote, author) VALUES ('If you don''t stand for something you will fall for anything.', 'Gordon Eadie' );

INSERT INTO quotes(quote, author) VALUES ('I may not have gone where I intended to go, but I think I have ended up where I needed to be.', 'Douglas Adams');
INSERT INTO quotes(quote, author) VALUES ('I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.', 'Dr. Seuss' );
INSERT INTO quotes(quote, author) VALUES ('That which does not kill us makes us stronger.', 'Friedrich Nietzsche' );
INSERT INTO quotes(quote, author) VALUES ('If you judge people, you have no time to love them.', 'Mother Teresa' );
INSERT INTO quotes(quote, author) VALUES ('For every minute you are angry you lose sixty seconds of happiness.', 'Ralph Waldo Emerson' );
INSERT INTO quotes(quote, author) VALUES ('Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.', 'Lao Tzu');
INSERT INTO quotes(quote, author) VALUES ('It is never too late to be what you might have been.', 'George Eliot' );
INSERT INTO quotes(quote, author) VALUES ('Women and cats will do as they please, and men and dogs should relax and get used to the idea.', 'Robert Heinlein' );
INSERT INTO quotes(quote, author) VALUES ('If you can''t explain it to a six year old, you don''t understand it yourself.', 'Albert Einstein' );
INSERT INTO quotes(quote, author) VALUES ('We don''t see things as they are, we see them as we are.', 'Anais Nin' );

INSERT INTO quotes(quote, author) VALUES ('All you need is love. But a little chocolate now and then doesn''t hurt.', 'Charles M. Schultz');
INSERT INTO quotes(quote, author) VALUES ('Everything you can imagine is real.', 'Pablo Picasso' );
INSERT INTO quotes(quote, author) VALUES ('Whenever I feel the need to exercise, I lie down until it goes away.', 'Paul Terry' );
INSERT INTO quotes(quote, author) VALUES ('One good thing about music, when it hits you, you feel no pain.', 'Bob Marley' );
INSERT INTO quotes(quote, author) VALUES ('The truth is, everyone is going to hurt you. You just got to find the ones worth suffering for.', 'Bob Marley' );
INSERT INTO quotes(quote, author) VALUES ('If you only read the books that everyone else is reading, you can only think what everyone else is thinking.', 'Haruki Murakami');
INSERT INTO quotes(quote, author) VALUES ('Life isn''t about finding yourself. Life is about creating yourself.', 'George Bernard Shaw' );
INSERT INTO quotes(quote, author) VALUES ('There is no friend as loyal as a book.', 'Ernest Hemingway' );
INSERT INTO quotes(quote, author) VALUES ('Success is not final, failure is not fatal: it is the courage to continue that counts.', 'Winston Churchill' );
INSERT INTO quotes(quote, author) VALUES ('Some people never go crazy. What truly horrible lives they must lead.', 'Charles Bukowski' );

INSERT INTO quotes(quote, author) VALUES ('You may say I''m a dreamer, but I''m not the only one. I hope someday you''ll join us. And the world will live as one.', 'John Lennon');
INSERT INTO quotes(quote, author) VALUES ('But better to get hurt by the truth than comforted with a lie.', 'Khaled Hosseini' );
INSERT INTO quotes(quote, author) VALUES ('Not all those who wander are lost.', 'J.R.R. Tolkien' );
INSERT INTO quotes(quote, author) VALUES ('If there''s a book that you want to read, but it hasn''t been written yet, then you must write it.', 'Toni Morrison' );
INSERT INTO quotes(quote, author) VALUES ('When I started counting my blessings, my whole life turned around.', 'Willie Nelson');
INSERT INTO quotes(quote, author) VALUES ('Today is the first day of the rest of your life.', 'Charles Dederich' );
INSERT INTO quotes(quote, author) VALUES ('Knowing yourself is the beginning of all wisdom.', 'Aristotle' );
INSERT INTO quotes(quote, author) VALUES ('Creativity is knowing how to hide your sources', 'C.E.M. Joad' );
INSERT INTO quotes(quote, author) VALUES ('I speak to everyone in the same way, whether he is the garbage man or the president of the university.', 'Albert Einstein' );
INSERT INTO quotes(quote, author) VALUES ('The secret to getting ahead, is getting started.', 'Mark Twain');

INSERT INTO quotes(quote, author) VALUES ('You show me a capitalist, and I''ll show you a bloodsucker.', 'Malcolm X');
INSERT INTO quotes(quote, author) VALUES ('The best friend a man has is his dog.', 'George Graham Vest' );
INSERT INTO quotes(quote, author) VALUES ('The customer is always right.', 'Harry Gordon Selfridge' );
INSERT INTO quotes(quote, author) VALUES ('Friends don''t let friends drive drunk.', 'public service ad slogan' );
INSERT INTO quotes(quote, author) VALUES ('Give me liberty or give me death!', 'Patrick Henry' );
INSERT INTO quotes(quote, author) VALUES ('Seize the day, boys. Make your lives extraordinary.', 'John Keating' );
INSERT INTO quotes(quote, author) VALUES ('I don''t care what they say as long as they talk about me.', 'Tallulah Bankhead' );
INSERT INTO quotes(quote, author) VALUES ('People are illogical, unreasonable, and self-centered. Love them anyway.', 'Kent M. Keith' );
INSERT INTO quotes(quote, author) VALUES ('To avoid criticism, say nothing, do nothing, be nothing.', 'Fred Shero' );
INSERT INTO quotes(quote, author) VALUES ('The most difficult years of marriage are those following the wedding.', 'Bethany Austin' );

INSERT INTO quotes(quote, author) VALUES ('It''s not whether you get knocked down; it''s whether you get up.', 'Vince Lombardi');
INSERT INTO quotes(quote, author) VALUES ('Only he who can see the invisible can do the impossible.', 'Frank L. Gaines' );
INSERT INTO quotes(quote, author) VALUES ('You have to do something in your life that is honorable and not cowardly if you are to live in peace with yourself.', 'Larry Brown' );
INSERT INTO quotes(quote, author) VALUES ('An athlete cannot run with money in his pockets. He must run with hope in his heart and dreams in his head.', 'Emil Zatopek' );
INSERT INTO quotes(quote, author) VALUES ('Set your goals high, and don''t stop till you get there.', 'Bo Jackson' );
INSERT INTO quotes(quote, author) VALUES ('The more difficult the victory, the greater the happiness in winning.', 'Pele' );
INSERT INTO quotes(quote, author) VALUES ('The will to win is important, but the will to prepare is vital.', 'Joe Paterno' );
INSERT INTO quotes(quote, author) VALUES ('I hated every minute of training, but I said, Don''t quit. Suffer now and live the rest of your life as a champion.', 'Muhammed Ali' );
INSERT INTO quotes(quote, author) VALUES ('Get busy living, or get busy dying.', 'Andy Dufresne' );
INSERT INTO quotes(quote, author) VALUES ('Everybody has a plan until they get punched in the mouth.', 'Mike Tyson');

INSERT INTO quotes(quote, author) VALUES ('Ask not what your country can do for you; ask what you can do for your country.', 'John F. Kennedy');
INSERT INTO quotes(quote, author) VALUES ('I am not a crook.', 'Richard Nixon');
INSERT INTO quotes(quote, author) VALUES ('Read my lips: no new taxes.', 'George H. W. Bush');
INSERT INTO quotes(quote, author) VALUES ('The fundamentals of the economy are strong.', 'John McCain');
INSERT INTO quotes(quote, author) VALUES ('Trying is the first step towards failure.', 'Homer Simpson');
INSERT INTO quotes(quote, author) VALUES ('The human race has one really effective weapon, and that is laughter.', 'Mark Twain');
INSERT INTO quotes(quote, author) VALUES ('You cannot run faster than a bullet.', 'Idi Amin');
INSERT INTO quotes(quote, author) VALUES ('There is no state with a democracy except Libya on the whole planet.', 'Muammar Gaddafi');
INSERT INTO quotes(quote, author) VALUES ('Politics is war without bloodshed while war is politics with bloodshed.', 'Mao Zedong');
INSERT INTO quotes(quote, author) VALUES ('I don''t care if they respect me so long as they fear me.', 'Caligula');

INSERT INTO quotes(quote, author) VALUES ('History is written by the victors.', 'Walter Benjamin');
INSERT INTO quotes(quote, author) VALUES ('One man with a gun can control 100 without one.', 'Vladimir Lenin');
INSERT INTO quotes(quote, author) VALUES ('A lie told often enough becomes the truth.', 'Vladimir Lenin');
INSERT INTO quotes(quote, author) VALUES ('I''m not a dictator. It''s just that I have a grumpy face.', 'Augusto Pinochet');
INSERT INTO quotes(quote, author) VALUES ('Never interrupt your enemy when he is making a mistake.', 'Napoleon Bonaparte');
INSERT INTO quotes(quote, author) VALUES ('Conquering the world on horseback is easy; it is dismounting and governing that is hard.', 'Genghis Khan');
INSERT INTO quotes(quote, author) VALUES ('If we don''t succeed, we run the risk of failure.', 'Dan Quayle');
INSERT INTO quotes(quote, author) VALUES ('Fiction writing is great, you can make up almost anything.', 'Ivana Trump');
INSERT INTO quotes(quote, author) VALUES ('Sure there have been injuries and deaths in boxing - but none of them serious.', 'Alan Minter');
INSERT INTO quotes(quote, author) VALUES ('Smoking kills. If you''re killed, you''ve lost a very important part of your life.', 'Brooke Shields');

INSERT INTO quotes(quote, author) VALUES ('Listen, everyone is entitled to my opinion.', 'Madonna');
INSERT INTO quotes(quote, author) VALUES ('I have opinions of my own but I don''t always agree with them.', 'George W. Bush');
INSERT INTO quotes(quote, author) VALUES ('He who stops being better stops being good.', 'Oliver Cromwell');
INSERT INTO quotes(quote, author) VALUES ('You can do anything, but not everything.', 'David Allen');
INSERT INTO quotes(quote, author) VALUES ('A wise man gets more use from his enemies than a fool from his friends.', 'Baltasar Gracian');
INSERT INTO quotes(quote, author) VALUES ('Everyone is a genius at least once a year. The real geniuses simply have their bright ideas closer together.', 'Georg Christoph Lichtenberg');
INSERT INTO quotes(quote, author) VALUES ('Believe those who are seeking the truth. Doubt those who find it.', 'Andre Gide');
INSERT INTO quotes(quote, author) VALUES ('I''d rather live with a good question than a bad answer.', 'Aryeh Frimer');
INSERT INTO quotes(quote, author) VALUES ('An inventor is simply a fellow who doesn''t take his education too seriously.', 'Charles F. Kettering');

INSERT INTO quotes(quote, author) VALUES ('Better to write for yourself and have no public, than to write for the public and have no self.', 'Cyril Connolly');
INSERT INTO quotes(quote, author) VALUES ('The cure for boredom is curiosity. There is no cure for curiosity.', 'Ellen Parr');
INSERT INTO quotes(quote, author) VALUES ('Advice is what we ask for when we already know the answer but wish we didn''t.', 'Erica Jong');
INSERT INTO quotes(quote, author) VALUES ('We are shaped and fashioned by what we love.', 'Goethe');
INSERT INTO quotes(quote, author) VALUES ('Love is being stupid together.', 'Paul Valery');
INSERT INTO quotes(quote, author) VALUES ('Where there is love there is no question.', 'Albert Einstein');
INSERT INTO quotes(quote, author) VALUES ('It is impossible to love and be wise.', 'Francis Bacon');
INSERT INTO quotes(quote, author) VALUES ('Death is not the worst that can happen to men.', 'Plato');
INSERT INTO quotes(quote, author) VALUES ('In this world, nothing is certain but death and taxes.', 'Benjamin Franklin');
INSERT INTO quotes(quote, author) VALUES ('Actors are the only honest hypocrites.', 'William Hazlitt');

INSERT INTO quotes(quote, author) VALUES ('The president of today is just the postage stamp of tomorrow.', 'Gracie Allen');
INSERT INTO quotes(quote, author) VALUES ('I know the human being and fish can coexist peacefully.', 'George W. Bush');
INSERT INTO quotes(quote, author) VALUES ('Our enemies are innovative and resourceful, and so are we.', 'George W. Bush');
INSERT INTO quotes(quote, author) VALUES ('Of those who say nothing, few are silent.', 'Thomas Neil');
INSERT INTO quotes(quote, author) VALUES ('I came, I saw, I conquered.', 'Julius Caesar');
INSERT INTO quotes(quote, author) VALUES ('Every strike brings me closer to the next home run.', 'Babe Ruth' );
INSERT INTO quotes(quote, author) VALUES ('Life is about making an impact, not making an income.', 'Kevin Kruse');
INSERT INTO quotes(quote, author) VALUES ('Life isn''t about getting and having, it’s about giving and being.', 'Kevin Kruse');
INSERT INTO quotes(quote, author) VALUES ('Life is 10% what happens to me and 90% of how I react to it.', 'Charles Swindoll');
INSERT INTO quotes(quote, author) VALUES ('The best revenge is massive success.', 'Frank Sinatra');

INSERT INTO quotes(quote, author) VALUES ('The proletarians have nothing to loose but their chains. They have a world to win.', 'Karl Marx');
INSERT INTO quotes(quote, author) VALUES ('People often say that motivation doesn''t last. Well, neither does bathing.  That’s why we recommend it daily.', 'Zig Ziglar');
INSERT INTO quotes(quote, author) VALUES ('The only person you are destined to become is the person you decide to be.', 'Ralph Waldo Emerson');
INSERT INTO quotes(quote, author) VALUES ('Few things can help an individual more than to place responsibility on him, and to let him know that you trust him.', 'Booker T. Washington');
INSERT INTO quotes(quote, author) VALUES ('Challenges are what make life interesting and overcoming them is what makes life meaningful. ', 'Joshua J. Marine');
INSERT INTO quotes(quote, author) VALUES ('Education costs money. But then so does ignorance. ', 'Sir Claus Moser');
INSERT INTO quotes(quote, author) VALUES ('You may be disappointed if you fail, but you are doomed if you don''t try.', 'Beverly Sills' );
INSERT INTO quotes(quote, author) VALUES ('Change your thoughts and you change your world.', 'Norman Vincent Peale');
INSERT INTO quotes(quote, author) VALUES ('Physics isn''t the most important thing. Love is.', 'Richard Feynman');
INSERT INTO quotes(quote, author) VALUES ('A man who is certain he is right is almost sure to be wrong.', 'Michael Faraday');

INSERT INTO quotes(quote, author) VALUES ('An expert is a person who has made all the mistakes that can be made in a very narrow field.', 'Niels Bohr');
INSERT INTO quotes(quote, author) VALUES ('There are some things so serious that you have to laugh at them.', 'Niels Bohr');
INSERT INTO quotes(quote, author) VALUES ('How wonderful that we have met with a paradox. Now we have some hope of making progress.', 'Niels Bohr');
INSERT INTO quotes(quote, author) VALUES ('Everything we call real is made of things that cannot be regarded as real.', 'Niels Bohr');
INSERT INTO quotes(quote, author) VALUES ('We are all agreed that your theory is crazy. The question is whether it is crazy enough to have a chance of being correct.', 'Niels Bohr');
INSERT INTO quotes(quote, author) VALUES ('An expert is someone who knows some of the worst mistakes that can be made in his subject, and how to avoid them.', 'Werner Heisenbeg');
INSERT INTO quotes(quote, author) VALUES ('Few, but ripe.', 'Carl Friedrich Gauss');
INSERT INTO quotes(quote, author) VALUES ('If I love you, what business is it of yours?', 'Goethe');
INSERT INTO quotes(quote, author) VALUES ('In the midst of chaos, there is also opportunity.', 'Sun Tzu');
INSERT INTO quotes(quote, author) VALUES ('Advertising is legalized lying.', 'H.G. Wells');

INSERT INTO quotes(quote, author) VALUES ('The theory of the Communists may be summed up in the single sentence: Abolition of private property.', 'Karl Marx');
INSERT INTO quotes(quote, author) VALUES ('Democracy is the road to socialism.', 'Karl Marx');
INSERT INTO quotes(quote, author) VALUES ('One finds limits by pushing them.', 'Herbert Simon');
INSERT INTO quotes(quote, author) VALUES ('There’s no shortage of remarkable ideas, what’s missing is the will to execute them.', 'Seth Godin');
INSERT INTO quotes(quote, author) VALUES ('You must either modify your dreams or magnify your skills.', 'Jim Rohn');
INSERT INTO quotes(quote, author) VALUES ('A business has to be involving, it has to be fun, and it has to exercise your creative instincts.', 'Richard Branson');
INSERT INTO quotes(quote, author) VALUES ('People rarely buy what they need. They buy what they want.', 'Seth Godin');
INSERT INTO quotes(quote, author) VALUES ('A man should never neglect his family for business. ', 'Walt Disney');
INSERT INTO quotes(quote, author) VALUES ('Please think about your legacy, because you''re writing it every day.', 'Gary Vaynerchuck');
INSERT INTO quotes(quote, author) VALUES ('Victory goes to the player who makes the next–to–last mistake.', 'Savielly Grigorievitch Tartakower');

INSERT INTO quotes(quote, author) VALUES ('I like thinking big. If you’re going to be thinking anything, you might as well think big.', 'Donald Trump');
INSERT INTO quotes(quote, author) VALUES ('Your income is directly related to your philosophy, NOT the economy.', 'Jim Rohn');
INSERT INTO quotes(quote, author) VALUES ('The golden rule for every business man is this: Put yourself in your customer''s place.', 'Orison Swett Marden');
INSERT INTO quotes(quote, author) VALUES ('People are best convinced by things they themselves discover.', 'Benjamin Franklin');
INSERT INTO quotes(quote, author) VALUES ('JUST DO IT!', 'Shia LaBeouf');
INSERT INTO quotes(quote, author) VALUES ('In order to become the master, the politician poses as the servant.', 'Charles de Gaulle');
INSERT INTO quotes(quote, author) VALUES ('Truth is not determined by majority vote.', 'Doug Gwyn');
INSERT INTO quotes(quote, author) VALUES ('We have, I fear, confused power with greatness.', 'Stewart Udall');
INSERT INTO quotes(quote, author) VALUES ('There are far too many men in politics and not enough elsewhere.', 'Hermione Gingold');
INSERT INTO quotes(quote, author) VALUES ('Show me someone without an ego, and I''ll show you a loser.”', 'Donald Trump');

INSERT INTO quotes(quote, author) VALUES ('What separates the winners from the losers is how a person reacts to each new twist of fate.', 'Donald Trump');
INSERT INTO quotes(quote, author) VALUES ('It doesn''t hurt to get more education.', 'Donald Trump');
INSERT INTO quotes(quote, author) VALUES ('Everything in life is luck.', 'Donald Trump');
INSERT INTO quotes(quote, author) VALUES ('Anyone who thinks my story is anywhere near over is sadly mistaken.', 'Donald Trump');
INSERT INTO quotes(quote, author) VALUES ('And if it can''t be fun, what''s the point?', 'Donald Trump');
INSERT INTO quotes(quote, author) VALUES ('Success comes from failure, not from memorizing the right answers.', 'Donald Trump');
INSERT INTO quotes(quote, author) VALUES ('The more predictable the business, the more valuable it is.', 'Donald Trump');
INSERT INTO quotes(quote, author) VALUES ('Building a brand may be more important than building a business.', 'Donald Trump');
INSERT INTO quotes(quote, author) VALUES ('A change is brought about because ordinary people do extraordinary things.', 'Barack Obama');

INSERT INTO quotes(quote, author) VALUES ('Nothing can stand in the way of the power of millions of voices calling for change.', 'Barack Obama');
INSERT INTO quotes(quote, author) VALUES ('Change is never easy, but always possible.', 'Barack Obama');
INSERT INTO quotes(quote, author) VALUES ('When our memories outweigh our dreams, it is then that we become old.', 'Bill Clinton');
INSERT INTO quotes(quote, author) VALUES ('Technology enables man to gain control over everything except technology.', 'Evan Esar');
INSERT INTO quotes(quote, author) VALUES ('Those who don''t know history are doomed to repeat it.', 'Edmund Burke');
INSERT INTO quotes(quote, author) VALUES ('Rudeness is the weak man’s imitation of strength.', 'Edmund Burke');
INSERT INTO quotes(quote, author) VALUES ('An intelligent man believes only half of what he hears, a wise man knows which half.', 'Evan Esar');
INSERT INTO quotes(quote, author) VALUES ('I never learned anything while I was talking.', 'Larry King');
INSERT INTO quotes(quote, author) VALUES ('You can''t stay mad at someone who makes you laugh.', 'Jay Leno');
INSERT INTO quotes(quote, author) VALUES ('The purpose of a writer is to keep civilization from destroying itself.', 'Albert Camus');

INSERT INTO quotes(quote, author) VALUES ('I believe empathy is the most essential quality of civilization.', 'Roger Ebert');
INSERT INTO quotes(quote, author) VALUES ('We are born princes and the civilizing process makes us frogs.', 'Eric Berne');
INSERT INTO quotes(quote, author) VALUES ('Without the library, you have no civilization.', 'Ray Bradbury');
INSERT INTO quotes(quote, author) VALUES ('Dare to think for yourself.', 'Voltaire');
INSERT INTO quotes(quote, author) VALUES ('The most important decision you make is to be in a good mood.', 'Voltaire');
INSERT INTO quotes(quote, author) VALUES ('The secret of being a bore is to tell everything.', 'Voltaire');
INSERT INTO quotes(quote, author) VALUES ('Prejudices are what fools use for reason.', 'Voltaire');
INSERT INTO quotes(quote, author) VALUES ('Liberty of thought is the life of the soul.', 'Voltaire');
INSERT INTO quotes(quote, author) VALUES ('The best way to predict your future is to create it.', 'Peter Drucker');
INSERT INTO quotes(quote, author) VALUES ('Being entirely honest with oneself is a good exercise.', 'Sigmund Freud');
INSERT INTO quotes(quote, author) VALUES ('The madman is a dreamer awake.', 'Sigmund Freud');

INSERT INTO quotes(quote, author) VALUES ('History will be kind to me for I intend to write it.', 'Winston Churchill');
INSERT INTO quotes(quote, author) VALUES ('If you don''t know history, then you don''t know anything. You are a leaf that doesn''t know it is part of a tree.', 'Michael Crichton');
INSERT INTO quotes(quote, author) VALUES ('Thus with a kiss I die.', 'William Shakespeare');
INSERT INTO quotes(quote, author) VALUES ('Creativity is allowing yourself to make mistakes. Art is knowing which ones to keep. ', 'Scott Adams');
INSERT INTO quotes(quote, author) VALUES ('Painting is just another way of keeping a diary.', 'Pablo Picasso');
INSERT INTO quotes(quote, author) VALUES ('Painting is poetry that is seen rather than felt, and poetry is painting that is felt rather than seen.', 'Leonardo da Vinci');
INSERT INTO quotes(quote, author) VALUES ('I don''t paint things. I only paint the difference between things. ', 'Henri Matisse');
INSERT INTO quotes(quote, author) VALUES ('All art requires courage.', 'Anne Tucker');
INSERT INTO quotes(quote, author) VALUES ('If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.', 'John von Neumann');
INSERT INTO quotes(quote, author) VALUES ('Go down deep enough into anything and you will find mathematics.', 'Dean Schlicter');

INSERT INTO quotes(quote, author) VALUES ('Some day you will be old enough to start reading fairy tales again.', 'Peter Drucker');
INSERT INTO quotes(quote, author) VALUES ('Boredom: the desire for desires.', 'Leo Tolstoy');
INSERT INTO quotes(quote, author) VALUES ('The best argument against democracy is a five-minute conversation with the average voter.', 'Winston Churchill');
INSERT INTO quotes(quote, author) VALUES ('History is the sum total of the things that could have been avoided.', 'Konrad Adenauer');
INSERT INTO quotes(quote, author) VALUES ('A problem is a chance for you to do your best.', 'Duke Ellington');
INSERT INTO quotes(quote, author) VALUES ('I always prefer to believe the best of everybody, it saves so much trouble.', 'Rudyard Kipling');
INSERT INTO quotes(quote, author) VALUES ('At his best, man is the noblest of all animals; separated from law and justice he is the worst.','Aristotle');
INSERT INTO quotes(quote, author) VALUES ('Knowing your own darkness is the best method for dealing with the darknesses of other people.', 'Carl Jung');
INSERT INTO quotes(quote, author) VALUES ('To love and win is the best thing. To love and lose, the next best.', 'William Makepeace Thackeray');
INSERT INTO quotes(quote, author) VALUES ('The days you work are the best days.', 'Georgia O''Keeffe');

INSERT INTO quotes(quote, author) VALUES ('The best intelligence test is what we do with our leisure.', 'Laurence J. Peter');
INSERT INTO quotes(quote, author) VALUES ('The best way of removing negativity is to laugh and be joyous.', 'David Icke');
INSERT INTO quotes(quote, author) VALUES ('At its best, life is completely unpredictable.', 'Christopher Walken');
INSERT INTO quotes(quote, author) VALUES ('Soap and water and common sense are the best disinfectants.', 'William Osler');
INSERT INTO quotes(quote, author) VALUES ('It is difficult to make our material condition better by the best law, but it is easy enough to ruin it by bad laws.', 'Theodore Roosevelt');
INSERT INTO quotes(quote, author) VALUES ('The best time to plan a book is while you''re doing the dishes.', 'Agatha Christie');
INSERT INTO quotes(quote, author) VALUES ('Getting married was the best thing I''ve ever done.','Megan Fox');
INSERT INTO quotes(quote, author) VALUES ('Ethical decisions ensure that everyone''s best interests are protected. When in doubt, don''t.', 'Harvey Mackay');
INSERT INTO quotes(quote, author) VALUES ('A satisfied customer is the best business strategy of all.', 'Michael LeBoeuf');
INSERT INTO quotes(quote, author) VALUES ('At the end of the day, my goal was to be the best hacker.', 'Kevin Mitnick');

INSERT INTO quotes(quote, author) VALUES ('I just want to do what I do best, and that''s fight. I love it.', 'Mike Tyson');
INSERT INTO quotes(quote, author) VALUES ('We''re not arrogant, we just believe we''re the best band in the world.', 'Noel Gallagher');
INSERT INTO quotes(quote, author) VALUES ('Some of my best leading men have been dogs and horses.', 'Elizabeth Taylor');
INSERT INTO quotes(quote, author) VALUES ('Negotiation means getting the best of your opponent.', 'Marvin Gaye');
INSERT INTO quotes(quote, author) VALUES ('The team with the best players wins.', 'Jack Welch');
INSERT INTO quotes(quote, author) VALUES ('The best way to remember your wife''s birthday is to forget it once.', 'E. Joseph Cossman');
INSERT INTO quotes(quote, author) VALUES ('The best kind of parent you can be is to lead by example.','Drew Barrymore');
INSERT INTO quotes(quote, author) VALUES ('I am the best. There is nobody better than me.', 'Floyd Mayweather, Jr.');
INSERT INTO quotes(quote, author) VALUES ('The best of us must sometimes eat our words.', 'J. K. Rowling');
INSERT INTO quotes(quote, author) VALUES ('I''m either going to go completely mental, completely bankrupt, or have the best success of my life.', 'Katy Perry');

INSERT INTO quotes(quote, author) VALUES ('If you deliver excellence right now, that gives you the best shot at the best future you''ve got coming.', 'Robert Forster');
INSERT INTO quotes(quote, author) VALUES ('The best present a man can give a woman is his undivided attention.', 'Usher');
INSERT INTO quotes(quote, author) VALUES ('The best substitute for experience is being sixteen.', 'Raymond Duncan');
INSERT INTO quotes(quote, author) VALUES ('Your best teacher is your last mistake.', 'Ralph Nader');
INSERT INTO quotes(quote, author) VALUES ('Science is the best idea humans have ever had. The more people who embrace that idea, the better.', 'Bill Nye');
INSERT INTO quotes(quote, author) VALUES ('Sometimes you get the best light from a burning bridge.', 'Don Henley');
INSERT INTO quotes(quote, author) VALUES ('To study the abnormal is the best way of understanding the normal.','William James');
INSERT INTO quotes(quote, author) VALUES ('People ask me, when was my best time? I always say: Today.', 'Paul Mooney');
INSERT INTO quotes(quote, author) VALUES ('People tend to play in their comfort zone, so the best things are achieved in a state of surprise, actually.', 'Brian Eno');
INSERT INTO quotes(quote, author) VALUES ('In any team sport, the best teams have consistency and chemistry.', 'Roger Staubach');

INSERT INTO quotes(quote, author) VALUES ('My best vacation is somewhere I could hide, somewhere warm and not a lot of people around.', 'Derek Jeter');
INSERT INTO quotes(quote, author) VALUES ('Government, even in its best state, is but a necessary evil; in its worst state, an intolerable one.', 'Thomas Paine');
INSERT INTO quotes(quote, author) VALUES ('Love is the only force capable of transforming an enemy into friend.', 'Martin Luther King, Jr.');
INSERT INTO quotes(quote, author) VALUES ('In the end, we will remember not the words of our enemies, but the silence of our friends.', 'Martin Luther King, Jr.');
INSERT INTO quotes(quote, author) VALUES ('Action is the foundational key to all success.', 'Pablo Picasso');
INSERT INTO quotes(quote, author) VALUES ('Success is a lousy teacher. It seduces smart people into thinking they can''t lose.', 'Bill Gates');
INSERT INTO quotes(quote, author) VALUES ('Always bear in mind that your own resolution to succeed is more important than any other.', 'Abraham Lincoln');
INSERT INTO quotes(quote, author) VALUES ('If your actions inspire others to dream more, learn more, do more and become more, you are a leader.', 'John Quincy Adams');
INSERT INTO quotes(quote, author) VALUES ('I am not afraid of an army of lions led by a sheep; I am afraid of an army of sheep led by a lion.', 'Alexander the Great');
INSERT INTO quotes(quote, author) VALUES ('The task of the leader is to get his people from where they are to where they have not been.', 'Henry A. Kissinger');

INSERT INTO quotes(quote, author) VALUES ('I suppose leadership at one time meant muscles; but today it means getting along with people.', 'Mahatma Gandhi');
INSERT INTO quotes(quote, author) VALUES ('The aim of education is the knowledge, not of facts, but of values.', 'William S. Burroughs');
INSERT INTO quotes(quote, author) VALUES ('I do not need a trophy to tell myself that I am the best.', 'Zlatan Ibrahimovic');
INSERT INTO quotes(quote, author) VALUES ('I don''t like to talk about myself.', 'Zlatan Ibrahimovic');
INSERT INTO quotes(quote, author) VALUES ('Zlatan doesn''t do auditions.', 'Zlatan Ibrahimovic');
INSERT INTO quotes(quote, author) VALUES ('Whenever life''s at a standstill, I need some action.', 'Zlatan Ibrahimovic');
INSERT INTO quotes(quote, author) VALUES ('If you are different, or you have minimum possibilities, you can still succeed. I am living proof of that.', 'Zlatan Ibrahimovic');
INSERT INTO quotes(quote, author) VALUES ('I''m like the wine. The older I get, the better I get.', 'Zlatan Ibrahimovic');
INSERT INTO quotes(quote, author) VALUES ('I always drive like a madman.', 'Zlatan Ibrahimovic');
INSERT INTO quotes(quote, author) VALUES ('A great leader is dead, a great Nation must move on.', 'Lyndon B. Johnson');

INSERT INTO quotes(quote, author) VALUES ('Laugh and the world laughs with you.', 'Ella Wheeler Wilcox');
INSERT INTO quotes(quote, author) VALUES ('We should weep for men at their birth, not at their death.', 'Baron de Montesquieu');
INSERT INTO quotes(quote, author) VALUES ('We are all self-made, but only the successful will admit it.', 'Earl Nightingale');
INSERT INTO quotes(quote, author) VALUES ('Banning a hobo costume doesn''t make the homeless feel better, it makes you feel better.', 'Bill Maher');
INSERT INTO quotes(quote, author) VALUES ('Anything worth doing is worth doing poorly, until you can learn to do it well.', 'Ziglar');
INSERT INTO quotes(quote, author) VALUES ('Never wish life were easier, wish that you were better.', 'Jim Rohn');
INSERT INTO quotes(quote, author) VALUES ('It''s better to be unhappy alone than unhappy with someone.', 'Marilyn Monroe');
INSERT INTO quotes(quote, author) VALUES ('The true soldier fights not because he hates what is in front of him, but because he loves what is behind him.', 'G.K. Chesterton');
INSERT INTO quotes(quote, author) VALUES ('Patriotism is the virtue of the vicious.', 'Oscar Wilde');
INSERT INTO quotes(quote, author) VALUES ('What can I tell you? Don''t piss off a motivated stripper.', 'Michael Clayton');

INSERT INTO quotes(quote, author) VALUES ('You never fail until you stop trying.', 'Albert Einstein');
INSERT INTO quotes(quote, author) VALUES ('There is no bad audience, just bad speakers.', 'J. Lloyd');
INSERT INTO quotes(quote, author) VALUES ('I can accept failure, everyone fails at something but I can’t accept not trying.', 'Michael Jordan');
INSERT INTO quotes(quote, author) VALUES ('Beauty is when you can appreciate yourself. When you love yourself, that''s when you''re most beautiful.', 'Zoe Kravitz');
INSERT INTO quotes(quote, author) VALUES ('Keep your goals in front of you and your fears behind you.', 'Tony Robbins');
INSERT INTO quotes(quote, author) VALUES ('It doesn’t matter where you are coming from. All that matters is where you are going.', 'Brian Tracy');
INSERT INTO quotes(quote, author) VALUES ('Yesterday is not ours to recover, but tomorrow is ours to win or lose.', 'Lyndon B. Johnson');
INSERT INTO quotes(quote, author) VALUES ('It is only through labor and painful effort, by grim energy and resolute courage, that we move on to better things.', 'Theodore Roosevelt');
INSERT INTO quotes(quote, author) VALUES ('If you’re offered a seat on a rocket ship, don’t ask what seat. Just get on.', 'Eric Schmidt');
INSERT INTO quotes(quote, author) VALUES ('There is nothing more freeing and empowering than learning to like your own company.', 'Mandy Hale');

INSERT INTO quotes(quote, author) VALUES ('The most dangerous worldview is the worldview of those who have not viewed the world.', 'Alexander von Humboldt');
INSERT INTO quotes(quote, author) VALUES ('If I can''t do it, it can''t be done.', '50 Cent');
INSERT INTO quotes(quote, author) VALUES ('Laughing at our mistakes can lengthen our own life. Laughing at someone else’s can shorten it.', 'Cullen Hightower');
INSERT INTO quotes(quote, author) VALUES ('If you can dream it, you can do it.', 'Walt Disney');
INSERT INTO quotes(quote, author) VALUES ('People Just Want to Connect.', 'Tom Segura');
INSERT INTO quotes(quote, author) VALUES ('Ask me a question in latin and I will answer you in greek.', 'Robert Oppenheimer');
INSERT INTO quotes(quote, author) VALUES ('They invented hugs to let people know you love them without saying anything.', 'Bil Keane');
INSERT INTO quotes(quote, author) VALUES ('Silence is one of the hardest arguments to refute.', 'Josh Billings');
INSERT INTO quotes(quote, author) VALUES ('Strength and growth come only through continuous effort and struggle.', 'Napoleon Hill');
INSERT INTO quotes(quote, author) VALUES ('Practice isn''t the thing you do once you''re good. It''s the thing you do that makes you good.', 'M. Gladwell');

INSERT INTO quotes(quote, author) VALUES ('The wealthiest place on the planet is the graveyard.', 'Les Brown');
INSERT INTO quotes(quote, author) VALUES ('Friends show their love in times of trouble, not in happiness.', 'Euripides');
INSERT INTO quotes(quote, author) VALUES ('A person doesn''t die when he should but when he can.', 'Gabriel García Márquez');
INSERT INTO quotes(quote, author) VALUES ('Knowing who you are is an extremely important skill.', 'Robert Greene');
INSERT INTO quotes(quote, author) VALUES ('Art consists of limitation. The most beautiful part of every picture is the frame.', 'Gilbert K. Chesterton');
INSERT INTO quotes(quote, author) VALUES ('Remember who you are.', 'Mufasa');
INSERT INTO quotes(quote, author) VALUES ('The best argument against Democracy is a 5 minute conversation with the average voter.', 'Winston Churchill');
INSERT INTO quotes(quote, author) VALUES ('Be polite, be professional, but have a plan to kill everybody you meet.', 'General Mad Dog James Mattis');
INSERT INTO quotes(quote, author) VALUES ('War does not determine who is right, only who is left.', 'Bertrand Russell');
INSERT INTO quotes(quote, author) VALUES ('A man with one watch knows what time it is; a man with two watches is never quite sure.', 'Lee Segall');

INSERT INTO quotes(quote, author) VALUES ('Learning never exhausts the mind.', 'Leonardo da Vinci');
INSERT INTO quotes(quote, author) VALUES ('Chop your own wood and it''ll warm you twice.', 'Henry ford');
INSERT INTO quotes(quote, author) VALUES ('The greatest weapon against stress is our ability to choose one thought over another.', 'William James');
INSERT INTO quotes(quote, author) VALUES ('Low self esteem is like driving through life with your hand-break on.', 'Maxwell Maltz');
INSERT INTO quotes(quote, author) VALUES ('I have found that if you love life, life will love you back', 'Arthur Rubinstein');
INSERT INTO quotes(quote, author) VALUES ('Following your heart also means eliminating the things that no longer evolve you.', 'Erykah Badu');
INSERT INTO quotes(quote, author) VALUES ('The only thing wrong with immortality is that it tends to go on forever.', 'Herb Caen');
INSERT INTO quotes(quote, author) VALUES ('Be weird. Your strangeness is your magic.', 'Parker Lewis');
INSERT INTO quotes(quote, author) VALUES ('It''s not what you look at that matters, it''s what you see.', 'Henry David Thoreau');
INSERT INTO quotes(quote, author) VALUES ('The ability to speak does not make you intelligent.', 'Qui-Gon Jinn');

INSERT INTO quotes(quote, author) VALUES ('One can measure the importance of a scientific work by the number of earlier publications rendered superfluous by it.', 'David Hilbert');
INSERT INTO quotes(quote, author) VALUES ('Beware the fury of a patient man', 'John Dryden');
INSERT INTO quotes(quote, author) VALUES ('Extinction is the rule. Survival is the exception.', 'Carl Sagan');
INSERT INTO quotes(quote, author) VALUES ('It is always the start that requires the greatest effort.', 'James Cash Penney');
INSERT INTO quotes(quote, author) VALUES ('Never underestimate the power of stupid people in large groups.', 'George Carlin');
INSERT INTO quotes(quote, author) VALUES ('Question everything. Learn something. Answer nothing.', 'Euripides');
INSERT INTO quotes(quote, author) VALUES ('To be happy, we must not be too concerned with others.', 'Albert Camus');
INSERT INTO quotes(quote, author) VALUES ('All photographs are accurate, but none of them is the truth.', 'Richard Avedon');
INSERT INTO quotes(quote, author) VALUES ('Opinion is the medium between knowledge and ignorance.', 'Plato');
INSERT INTO quotes(quote, author) VALUES ('Happiness is like a kiss. You must share it to enjoy it.', 'Bernard Meltzer');

INSERT INTO quotes(quote, author) VALUES ('Don''t pray for an easy life. Pray for the strength to endure a difficult one', 'Bruce Lee');
INSERT INTO quotes(quote, author) VALUES ('I have immeasurable faith in humanity''s capacity for depravity',  'Alber J Torres');
INSERT INTO quotes(quote, author) VALUES ('Politicians and diapers must be changed often, and for the same reason.', 'Mark Twain');
INSERT INTO quotes(quote, author) VALUES ('The greatest good you can do for another is not just share your riches, but to reveal to him his own.', 'Benjamin Disraeli');
INSERT INTO quotes(quote, author) VALUES ('We Become What We Think About.', 'Earl Nightingale');
INSERT INTO quotes(quote, author) VALUES ('The medicine for my suffering I had within me from the very beginning', 'Bruce Lee');
INSERT INTO quotes(quote, author) VALUES ('It is amazing how complete is the delusion that beauty is goodness.', 'Leo Tolstoy');
INSERT INTO quotes(quote, author) VALUES ('Education is the most powerful weapon which you can use to change the world.', 'Nelson Mandela');
INSERT INTO quotes(quote, author) VALUES ('Work gives you meaning and purpose and life is empty without it.', 'Stephen Hawking');
INSERT INTO quotes(quote, author) VALUES ('Life is the art of drawing without an eraser', 'John W. Gardner');

INSERT INTO quotes(quote, author) VALUES ('If you want real peace in the world, start with children.', 'Mahatma Gandhi');
INSERT INTO quotes(quote, author) VALUES ('If you can not be positive then at least be quiet.', 'Joel Osteen');
INSERT INTO quotes(quote, author) VALUES ('An inventor is simply a fellow who doesn’t take his education too seriously.', 'Charles F. Kettering');
INSERT INTO quotes(quote, author) VALUES ('If you want to keep a secret, you must also hide it from yourself.', 'George Orwell');
INSERT INTO quotes(quote, author) VALUES ('The highest criterion of a civilization is its willingness to help the less fortunate people.', 'Booker T. Washington');
INSERT INTO quotes(quote, author) VALUES ('He who does not understand your silence will probably not understand your words.', 'Elbert Hubbard');
INSERT INTO quotes(quote, author) VALUES ('The art of being wise is the art of knowing what to overlook.', 'William James');
INSERT INTO quotes(quote, author) VALUES ('A day without laughter is a day wasted.', 'Nicolas Chamfort');
INSERT INTO quotes(quote, author) VALUES ('You must trust and believe in people or life becomes impossible.', 'Anton Chekhov');
INSERT INTO quotes(quote, author) VALUES ('Hope is being able to see that there is light despite all of the darkness.', 'Desmond Tutu');

INSERT INTO quotes(quote, author) VALUES ('A ship is safe in harbor, but that''s not what ships are made for.', 'John Shedd');
INSERT INTO quotes(quote, author) VALUES ('I''ve failed over and over and over again in my life and that is why I succeed.', 'Michael Jordan');
INSERT INTO quotes(quote, author) VALUES ('If you want total security, go to prison. There you''re fed and clothed. The only thing lacking is freedom.', 'Dwight D. Eisenhower');
INSERT INTO quotes(quote, author) VALUES ('The most common lies are the ones you tell yourself; Lying to others is an exception.', 'Friedrich Nietzsche');
INSERT INTO quotes(quote, author) VALUES ('A clever person solves a problem. A wise person avoids it.', 'Albert Einstein');
INSERT INTO quotes(quote, author) VALUES ('It is not flesh and blood, but heart which makes us fathers and sons.', 'Friedrich Schiller');
INSERT INTO quotes(quote, author) VALUES ('He who doesn''t believe himself always lies.', 'Friedrich Nietzsche');
INSERT INTO quotes(quote, author) VALUES ('After I learned about confirmation bias, I started seeing it everywhere.', 'Jon Ronson');
INSERT INTO quotes(quote, author) VALUES ('Your most unhappy customers are your greatest source of learning.', 'Bill Gates');
INSERT INTO quotes(quote, author) VALUES ('It would be a nice thing if humanity could survive.', 'Noam Chomsky');
INSERT INTO quotes(quote, author) VALUES ('The compensation for dying is that I will learn all the things I was not able to learn here on Earth.', 'Alexander Imich');

INSERT INTO quotes(quote, author) VALUES ('If you can''t feed a hundred people, feed just one.', 'Mother Teresa');
INSERT INTO quotes(quote, author) VALUES ('I would die for my country but I could never let my country die for me.', 'Neil Kinnock');
INSERT INTO quotes(quote, author) VALUES ('It is the cause, not the death, that makes the martyr.', 'Napoleon Bonaparte');
INSERT INTO quotes(quote, author) VALUES ('Education is the key to unlock the golden door of freedom.', 'George Washington Carver');
INSERT INTO quotes(quote, author) VALUES ('The first draft is nothing more than a starting point, so be wrong as fast as you can.', 'Andrew Stanton');
INSERT INTO quotes(quote, author) VALUES ('Don''t worry about failure; you only have to be right once.', 'Drew Houston');
INSERT INTO quotes(quote, author) VALUES ('When you do what you fear most, then you can do anything.', 'Stephen Richards');
INSERT INTO quotes(quote, author) VALUES ('Reality is wrong. Dreams are for real.', 'Tupac Shakur');
INSERT INTO quotes(quote, author) VALUES ('The future belongs to those who believe in the beauty of their dreams.', 'Eleanor Roosevelt');
INSERT INTO quotes(quote, author) VALUES ('What is freedom of expression? Without the freedom to offend, it ceases to exist.', 'Salman Rushdie');

INSERT INTO quotes(quote, author) VALUES ('You know your shortcomings yet You love yourself. How come you hate others for their shortcomings?', 'Swami Vivekananda');
INSERT INTO quotes(quote, author) VALUES ('If you do not change direction, you may end up where you are heading.', 'Lao Tzu');
INSERT INTO quotes(quote, author) VALUES ('A wise man can learn more from his enemies than a fool from his friends.', 'Niki Lauda');
INSERT INTO quotes(quote, author) VALUES ('You may have to fight a battle more than once to win it.', 'Margaret Thatcher');
INSERT INTO quotes(quote, author) VALUES ('The greatest happiness is to know the source of unhappiness.', 'Fyodor Dostoevsky');
INSERT INTO quotes(quote, author) VALUES ('You’ll never find peace of mind until you listen to your heart.', 'George Michael');
INSERT INTO quotes(quote, author) VALUES ('The greatest mistake you can make in life is to be continually fearing you will make one.', 'Elbert Hubbard');
INSERT INTO quotes(quote, author) VALUES ('You never understand anybody that loves you.', 'Ernest Hemingway');
INSERT INTO quotes(quote, author) VALUES ('My wife and I were happy for twenty years - then we met.', 'Rodney Dangerfield');
INSERT INTO quotes(quote, author) VALUES ('It’s a good idea always to do something relaxing prior to making an important decision in your life.', 'Paulo Coelho');

INSERT INTO quotes(quote, author) VALUES ('They lived and laughed and loved and left.', 'James Joyce');
INSERT INTO quotes(quote, author) VALUES ('All the problems in the world can be traced to what fathers do to their sons.', 'George Carlin');
INSERT INTO quotes(quote, author) VALUES ('Plans are worthless, but planning is everything.', 'Dwight D. Eisenhower');
INSERT INTO quotes(quote, author) VALUES ('I''m a success today because I had a friend who believed in me and I didn''t have the heart to let him down.', 'Abraham Lincoln');
INSERT INTO quotes(quote, author) VALUES ('Individually, we are one drop. Together, we are an ocean.', 'Ryunosuke Satoro');
INSERT INTO quotes(quote, author) VALUES ('History doesn''t repeat itself, but it does rhyme.', 'Mark Twain');
INSERT INTO quotes(quote, author) VALUES ('Imagination is more important than knowledge.', 'Albert Einstein');
INSERT INTO quotes(quote, author) VALUES ('If you make an effort and don''t receive any in return, then stop making an effort.', 'Gurpreet Ghotra');
INSERT INTO quotes(quote, author) VALUES ('Live each day as if it were your last.', 'Marcus Aurelius');
INSERT INTO quotes(quote, author) VALUES ('Happiness is not something you postpone for the future; it is something you design for the present.', 'Jim Rohn');

INSERT INTO quotes(quote, author) VALUES ('If you want to keep your sanity, never let yourself become overwhelmed by things you can’t control.', 'William Chapman');
INSERT INTO quotes(quote, author) VALUES ('Within you is a stillness and a sanctuary to which you can retreat at any time and be yourself.', 'Hermann Hesse');
INSERT INTO quotes(quote, author) VALUES ('When we are not sure, we are alive.', 'Graham Greene');
INSERT INTO quotes(quote, author) VALUES ('Chop your own wood and it will warm you twice.', 'Henry Ford');
INSERT INTO quotes(quote, author) VALUES ('Success is going from failure to failure without loss of enthusiasm.', 'Winston Churchill');
INSERT INTO quotes(quote, author) VALUES ('No one heals himself by wounding another.', 'St. Ambrose');
INSERT INTO quotes(quote, author) VALUES ('Love is when the other person''s happiness is more important than your own.', 'H. Jackson Brown, Jr.');
INSERT INTO quotes(quote, author) VALUES ('Authors write books for one, and only one, reason: because we like to torture people.', 'Brandon Sanderson');
INSERT INTO quotes(quote, author) VALUES ('He who controls the past controls the future. He who controls the present controls the past.', 'George Orwell');
INSERT INTO quotes(quote, author) VALUES ('You are the universe expressing itself as a human for a little while.', 'Eckhart Tolle');

INSERT INTO quotes(quote, author) VALUES ('We have to do more than just elect a new President if we truly want to change this country.', 'Dan Quayle');
INSERT INTO quotes(quote, author) VALUES ('The first thing to know about the supernatural is that it never appears when it will be incredibly well documented.', 'Max Post');
INSERT INTO quotes(quote, author) VALUES ('A man of courage never wants weapons.', 'Thomas Fuller');
INSERT INTO quotes(quote, author) VALUES ('Out of nothing I have created a strange new universe.', 'János Bolyai');
INSERT INTO quotes(quote, author) VALUES ('If you''re tired of arguing with strangers on the internet, try talking to one in real life.', 'Barack Obama');
INSERT INTO quotes(quote, author) VALUES ('It is often in the darkest skies that we see the brightest stars.', 'Richard Paul Evans');
INSERT INTO quotes(quote, author) VALUES ('There are two different types of people in the world, those who want to know, and those who want to believe.', 'Friedrich Nietzsche');
INSERT INTO quotes(quote, author) VALUES ('Sometimes people don''t want to hear the truth because they don''t want their illusions destroyed.', 'Friedrich Nietzsche');
INSERT INTO quotes(quote, author) VALUES ('Coming back to where you started is not the same as never leaving.', 'Terry Pratchett');
INSERT INTO quotes(quote, author) VALUES ('All morons hate it when you call them a moron.', 'Holden Caulfield');

INSERT INTO quotes(quote, author) VALUES ('The truth will set you free. But not until it is finished with you.', 'David Foster Wallace');
INSERT INTO quotes(quote, author) VALUES ('Inspiration is a guest that does not willingly visit the lazy.', 'Pyotr Tchaikovsky');
INSERT INTO quotes(quote, author) VALUES ('Never tell the truth to people who are not worthy of it.', 'Mark Twain');
INSERT INTO quotes(quote, author) VALUES ('Don''t listen to the cynics. They were wrong about my generation and they were wrong about yours.', 'Joe Biden');
INSERT INTO quotes(quote, author) VALUES ('Only those who dare to fail greatly can ever achieve greatly.', 'Robert Kennedy');
INSERT INTO quotes(quote, author) VALUES ('We have the marvelous gift of making everything insignificant.', 'Nikolai Gogol');
INSERT INTO quotes(quote, author) VALUES ('A man paints with his brains and not with his hands.', 'Michelangelo');
INSERT INTO quotes(quote, author) VALUES ('It is not the mountains ahead to climb that wear you out; it is the pebble in your shoe.', 'Muhammad Ali');
INSERT INTO quotes(quote, author) VALUES ('Stress can ruin every day of your life, dying can only ruin one.', 'Sherlock Holmes');
INSERT INTO quotes(quote, author) VALUES ('I love Humanity but I hate humans.', 'Albert Einstein');

INSERT INTO quotes(quote, author) VALUES ('I would rather walk with a friend in the dark, than alone in the light.', 'Helen Keller');
INSERT INTO quotes(quote, author) VALUES ('Attention is the rarest and purest form of generosity.', 'Simone Weil');
INSERT INTO quotes(quote, author) VALUES ('Nature is written in mathematical language.', 'Galileo Galilei');
INSERT INTO quotes(quote, author) VALUES ('You never know what is enough unless you know what is more than enough.', 'William Blake');
INSERT INTO quotes(quote, author) VALUES ('Men will always be mad, and those who think they can cure them are the maddest of all.', 'Voltaire');
INSERT INTO quotes(quote, author) VALUES ('Stay committed to your decisions, but stay flexible in your approach.', 'Tom Robbins');
INSERT INTO quotes(quote, author) VALUES ('The only way to have a friend is to be one.', 'Ralph Waldo Emerson');
INSERT INTO quotes(quote, author) VALUES ('Damn your principles, stick with your party!', 'Benjamin Disraeli');
INSERT INTO quotes(quote, author) VALUES ('By acting as if I was not afraid I gradually ceased to be afraid.', 'Theodore Roosevelt');
INSERT INTO quotes(quote, author) VALUES ('Peace for our time!', 'Neville Chamberlain');

INSERT INTO quotes(quote, author) VALUES ('The trouble with being punctual is that nobody’s there to appreciate it.', 'Franklin P. Jones');
INSERT INTO quotes(quote, author) VALUES ('If you want to be original Be ready to be copied.', 'Aphos');
INSERT INTO quotes(quote, author) VALUES ('The present is theirs; the future, for which I really worked, is mine.', 'Nikola Tesla');
INSERT INTO quotes(quote, author) VALUES ('Those who don''t believe in magic will never find it.', 'Roald Dahl');
INSERT INTO quotes(quote, author) VALUES ('A patriot must always be ready to defend his country against his government.', 'Edward Abbey');
INSERT INTO quotes(quote, author) VALUES ('Be yourself; everyone else is already taken.', 'Oscar Wilde');
INSERT INTO quotes(quote, author) VALUES ('Take the stones people throw at you, and use them to build a monument.', 'Ratan Tata');
INSERT INTO quotes(quote, author) VALUES ('I think life''s an irrational obsession.',  'Sean Penn');
INSERT INTO quotes(quote, author) VALUES ('A penny saved is a penny earned.', 'Benjamin Franklin');
INSERT INTO quotes(quote, author) VALUES ('Violence is the last refuge of the incompetent.', 'Isaac Asimov');

INSERT INTO quotes(quote, author) VALUES ('A really great man is known by three signs: generosity in the design, humanity in the execution, moderation in success.', 'Otto von Bismarck');
INSERT INTO quotes(quote, author) VALUES ('You are free, and that is why you are lost.', 'Franz Kafka');
INSERT INTO quotes(quote, author) VALUES ('Everyone has a plan until they get punched in the mouth.', 'Mike Tyson');
INSERT INTO quotes(quote, author) VALUES ('You can tell how smart people are by what they laugh at.', 'Tina Fey');
INSERT INTO quotes(quote, author) VALUES ('Alcohol, taken in sufficient quantities, may produce all the effects of drunkenness.', 'Oscal Wilde');
INSERT INTO quotes(quote, author) VALUES ('Those who can make you believe absurdities, can make you commit atrocities.', 'Voltaire');
INSERT INTO quotes(quote, author) VALUES ('Family is not an important thing. It''s everything.', 'Michael J. Fox');
INSERT INTO quotes(quote, author) VALUES ('It is easier to build strong children than to repair broken men.', 'Frederick Douglass');
INSERT INTO quotes(quote, author) VALUES ('Keep your eyes on the stars, and your feet on the ground.', 'Theodore Roosevel');




--Buddha
INSERT INTO quotes(quote, author) VALUES ('You yourself, as much as anybody in the entire universe, deserve your love and affection.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('You only lose what you cling to.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('No one saves us but ourselves. No one can and no one may. We ourselves must walk the path.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('Doubt everything. Find your own light.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('There is no path to happiness: happiness is the path.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('If you truly loved yourself, you could never hurt another.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('Pain is certain, suffering is optional.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('If we could see the miracle of a single flower clearly our whole life would change. ', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('Holding onto anger is like drinking poison and expecting the other person to die.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('The mind is everything. What you think you become.',  'Buddha');

INSERT INTO quotes(quote, author) VALUES ('A family is a place where minds come in contact with one another.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('The tongue like a sharp knife... Kills without drawing blood.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('Nothing is forever except change.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('With our thoughts we make the world.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('There is no fire like passion, there is no shark like hatred, there is no snare like folly, there is no torrent like greed.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('True love is born from understanding.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('The trouble is, you think you have time.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('Friendship is the only cure for hatred, the only guarantee of peace. ', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('People with opinions just go around bothering one another.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('It is better to travel, than to arrive.',  'Buddha');

INSERT INTO quotes(quote, author) VALUES ('Most problems, if you give them enough time and space, will eventually wear themselves out.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('Happiness does not depend on what you have or who you are, it solely relies on what you think.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('Whoever sees me sees the teaching, and whoever sees the teaching sees me.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('Resolutely train yourself to attain peace.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('If you are facing in the right direction, all you need to do is keep on walking.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('Every experience, no matter how bad it seems, holds within it a blessing of some kind. The goal is to find it.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('It is better to travel well than to arrive.', 'Buddha');


--Confucius
INSERT INTO quotes(quote, author) VALUES ('Everything has beauty, but not everyone can see.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('It does not matter how slowly you go as long as you do not stop.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('Only the wisest and stupidest of men never change.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('The strength of a nation derives from the integrity of the home.', 'Confucius' );
INSERT INTO quotes(quote, author) VALUES ('If you make a mistake and do not correct it, this is called a mistake.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('Life is really simple, but we insist on making it complicated.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('The funniest people are the saddest ones.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('You cannot open a book without learning something.', 'Confucius' );
INSERT INTO quotes(quote, author) VALUES ('The gem cannot be polished without friction, nor man perfected without trials.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('Forget injuries, never forget kindnesses.', 'Confucius' );

INSERT INTO quotes(quote, author) VALUES ('Education breeds confidence. Confidence breeds hope. Hope breeds peace.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('To be wealthy and honored in an unjust society is a disgrace.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('Never give a sword to a man who can''t dance.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('True wisdom is knowing what you don''t know', 'Confucius' );
INSERT INTO quotes(quote, author) VALUES ('A common man marvels at uncommon things. A wise man marvels at the commonplace.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('The superior man understands what is right; the inferior man understands what will sell.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('Don''t use cannon to kill musquito.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('Never tire to study. And to teach to others.', 'Confucius' );
INSERT INTO quotes(quote, author) VALUES ('All people are the same; only their habits differ.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('The journey with a 1000 miles begins with one step.', 'Confucius' );


--Dalai Lama
INSERT INTO quotes(quote, author) VALUES ('Remember that not getting what you want is sometimes a wonderful stroke of luck.', 'Dalai Lama');
INSERT INTO quotes(quote, author) VALUES ('If you think you are too small to make a difference, try sleeping with a mosquito.', 'Dalai Lama');
INSERT INTO quotes(quote, author) VALUES ('Choose to be optimistic, it feels better.', 'Dalai Lama');
INSERT INTO quotes(quote, author) VALUES ('The more you are motivated by love, the more fearless and free your action will be.', 'Dalai Lama');
INSERT INTO quotes(quote, author) VALUES ('Sleep is the best meditation.', 'Dalai Lama');
INSERT INTO quotes(quote, author) VALUES ('Where ignorance is our master, there is no possibility of real peace.', 'Dalai Lama');
INSERT INTO quotes(quote, author) VALUES ('It is not enough to be compassionate, we must act.', 'Dalai Lama');
INSERT INTO quotes(quote, author) VALUES ('The enemy is the necessary condition for practicing patience.', 'Dalai Lama');
INSERT INTO quotes(quote, author) VALUES ('I do not judge the universe.', 'Dalai Lama');
INSERT INTO quotes(quote, author) VALUES ('Happiness is not something ready made. It comes from your own actions.', 'Dalai Lama');


--proverbs
INSERT INTO quotes(quote, author) VALUES ('Never attribute to malice that which is adequately explained by stupidity.', 'Hanlon''s Razor');
INSERT INTO quotes(quote, author) VALUES ('The apple doesn''t fall far from the tree.', 'proverb');
INSERT INTO quotes(quote, author) VALUES ('The pen is mightier than the sword.', 'proverb');
INSERT INTO quotes(quote, author) VALUES ('Two wrongs don''t make a right.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('When the going gets tough, the tough get going.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('Fortune favors the bold.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('People who live in glass houses should not throw stones.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('Hope for the best, but prepare for the worst.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('Better late than never.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('A picture is worth a thousand words.', 'English proverb');

INSERT INTO quotes(quote, author) VALUES ('There''s no such thing as a free lunch.', 'English Proverb');
INSERT INTO quotes(quote, author) VALUES ('You can''t make an omelet without breaking a few eggs.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('Practice makes perfect.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('All good things must come to an end.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('Necessity is the mother of invention.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('Good things come to those who wait.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('Don''t put all your eggs in one basket.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('If you want something done right, you have to do it yourself.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('Great minds think alike.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('If you''re not part of the solution, you''re part of the problem.', 'English proverb');

INSERT INTO quotes(quote, author) VALUES ('What goes up must come down.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('You can''t teach an old dog new tricks.', 'English proverb');
INSERT INTO quotes(quote, author) VALUES ('Love is sweet torment.', 'English proverb');


--natural laws
INSERT INTO quotes(quote, author) VALUES ('Every object in a state of uniform motion tends to remain in that state of motion unless an external force is applied to it.', 'Newton''s I law');
INSERT INTO quotes(quote, author) VALUES ('The vector sum of the external forces on an object is equal to the product of mass and the acceleration vector of the object.', 'Newton''s II law');
INSERT INTO quotes(quote, author) VALUES ('For every action there is an equal and opposite reaction.', 'Newton''s III law');
INSERT INTO quotes(quote, author) VALUES ('Planets orbit the sun elliptically.', 'Kepler''s I law');
INSERT INTO quotes(quote, author) VALUES ('A line segment joining a planet and the Sun sweeps out equal areas during equal intervals of time.', 'Kepler''s II law');
INSERT INTO quotes(quote, author) VALUES ('The square of the orbital period of a planet is proportional to the cube of the axis of its orbit.', 'Kepler''s III law');
INSERT INTO quotes(quote, author) VALUES ('The force acting on a submerged object equals the weight of the displaced liquid.', 'Archimedes'' Buoyancy principle');
INSERT INTO quotes(quote, author) VALUES ('The total energy of an isolated system remains constant.', 'The law of conservation of energy');
INSERT INTO quotes(quote, author) VALUES ('whatever can go wrong, will go wrong.', 'Murphy''s Law');
INSERT INTO quotes(quote, author) VALUES ('Equal volumes of all gases at the same temperature and pressure contain equal numbers of molecules.', 'Avogadro''s hypothesis');

INSERT INTO quotes(quote, author) VALUES ('Objects attract each other with a force proportional to the product of masses and inversely proportional to the square distance.', 'law of gravitation');
INSERT INTO quotes(quote, author) VALUES ('The total current or charge entering a junction or node is exactly equal to the charge leaving the node.', 'Kirchoff''s I law');
INSERT INTO quotes(quote, author) VALUES ('In a closed loop network, the total voltage around the loop is equal to the sum of voltage drops within the loop.', 'Kirchoffs''s II law');
INSERT INTO quotes(quote, author) VALUES ('The product of the pressure and the volume of an ideal gas at constant temperature is a constant.', 'Boyle''s law');
INSERT INTO quotes(quote, author) VALUES ('The random motion of particles suspended in a fluid due to collisions with atoms or molecules in the liquid.', 'Brownian motion');
INSERT INTO quotes(quote, author) VALUES ('The volume of an ideal gas at constant pressure is proportional to the thermodynamic temperature of that gas.', 'Charles'' law');
INSERT INTO quotes(quote, author) VALUES ('The total mass-energy of a closed system remains constant.', 'Conservation of mass-energy');
INSERT INTO quotes(quote, author) VALUES ('The total electric charge of a closed system remains constant.', 'Conservation of electric charge');
INSERT INTO quotes(quote, author) VALUES ('The total linear momentum of a closed system remains constant.', 'Conservation of linear momentum');
INSERT INTO quotes(quote, author) VALUES ('The total angular momentum of a closed system remains constant.', 'Conservation of angular momentum');

INSERT INTO quotes(quote, author) VALUES ('The speed of light in vacuum is measured as the same speed to all observers, regardless of their relative motion.', 'Constancy principle');
INSERT INTO quotes(quote, author) VALUES ('The Sun, not the Earth, is at the center of the Universe.', 'Copernican principle');
INSERT INTO quotes(quote, author) VALUES ('The total pressure of a mixture of ideal gases is equal to the sum of the partial pressures of its components', 'Kirchoffs''s II law');
INSERT INTO quotes(quote, author) VALUES ('The product of the pressure and the volume of an ideal gas at constant temperature is constant.', 'Dalton''s Law of partial pressures');
INSERT INTO quotes(quote, author) VALUES ('The energy of a particle is equal to its mass times the square of the speed of light.', 'Einstein''s mass-energy equation');
INSERT INTO quotes(quote, author) VALUES ('The path taken by a ray of light between any two points in a system is always the path that takes the least time.', 'Fermat''s principle');
INSERT INTO quotes(quote, author) VALUES ('The electric flux through a closed surface is proportional to the sum of charges contained within the closed surface.', 'Gauss'' law');
INSERT INTO quotes(quote, author) VALUES ('The stress applied to any solid is proportional to the strain it produces within the elastic limit for that solid. ', 'Hooke''s law');
INSERT INTO quotes(quote, author) VALUES ('If two theories predict phenomena to the same accuracy, then the one which is simpler is the better one. ', 'Occam''s razor');
INSERT INTO quotes(quote, author) VALUES ('The current through a conductor between two points is directly proportional to the voltage across the two points', 'Ohm''s law');

INSERT INTO quotes(quote, author) VALUES ('In a hierarchy, every employee tends to rise to his level of incompetence.', 'Peter principle');
INSERT INTO quotes(quote, author) VALUES ('The ratio of a circle''s circumference to its diameter', 'pi');


--books
INSERT INTO quotes(quote, author) VALUES ('It was the best of times, it was the worst of times.', 'Charles Dickens, A Tale of Two Cities');
INSERT INTO quotes(quote, author) VALUES ('Someone must have slandered Josef K., for one morning, without having done anything truly wrong, he was arrested', 'Franz Kafka, The Trial');
INSERT INTO quotes(quote, author) VALUES ('All of this happened, more or less.', 'Kurt Vonnegut, Slaughterhouse-Five');
INSERT INTO quotes(quote, author) VALUES ('It was love at first sight.', 'Joseph Heller, Catch-22');
INSERT INTO quotes(quote, author) VALUES ('It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.', 'Jane Austen, Pride and Prejudice');
INSERT INTO quotes(quote, author) VALUES ('All happy families are alike; each unhappy family is unhappy in its own way.', 'Leo Tolstoy, Anna Karenina');
INSERT INTO quotes(quote, author) VALUES ('All children, except one, grow up.', 'J.M. Barrie, Peter Pan');
INSERT INTO quotes(quote, author) VALUES ('The schoolmaster was leaving the village, and everybody seemed sorry.', 'Thomas Hardy, Jude the Obscure');
INSERT INTO quotes(quote, author) VALUES ('There was no possibility of taking a walk that day.', 'Charlotte Bronte, Jane Eyre');
--INSERT INTO quotes(quote, author) VALUES ('He was an old man who fished alone in a skiff in the Gulf Stream and he had gone 84 days now without taking a fish.', 'Ernest Hemingway, The Old Man And The Sea');

INSERT INTO quotes(quote, author) VALUES ('It''s funny. Don''t ever tell anybody anything. If you do, you start missing everybody.', 'J.D. Salinger, The Cather in the Rye.');
INSERT INTO quotes(quote, author) VALUES ('We are what we pretend to be, so we must be very careful what we pretend to be', 'Kurt Vonnegut, Mother Night');


--poems
INSERT INTO quotes(quote, author) VALUES ('Roses are red, violets are blue. Sugar is sweet, and so are you.', 'Poem' );
INSERT INTO quotes(quote, author) VALUES ('Twinkle, twinkle, little star, how I wonder what you are! Up above the world so high, like a diamond in the sky.', 'Poem');
INSERT INTO quotes(quote, author) VALUES ('Now I know my ABCs. Next time won''t you sing with me? ', 'Alphabet Song');


--AFI's 100 Years...100 Movie Quotes
--https://en.wikipedia.org/wiki/AFI's_100_Years...100_Movie_Quotes
INSERT INTO quotes(quote, author) VALUES ('Frankly, my dear, I don''t give a damn.', 'Rhett Butler, Gone with the Wind'); 
INSERT INTO quotes(quote, author) VALUES ('I''m gonna make him an offer he can''t refuse.', 'Vito Corleone, The Godfather');
INSERT INTO quotes(quote, author) VALUES ('Here''s looking at you, kid.', 'Rick Blaine, Casablanca' );
INSERT INTO quotes(quote, author) VALUES ('Go ahead, make my day.', 'Harry Callahan, Dirty Harry' );
INSERT INTO quotes(quote, author) VALUES ('May the Force be with you.', 'Han Solo, Star Wars');
INSERT INTO quotes(quote, author) VALUES ('I love the smell of napalm in the morning.', 'Lt. Col. Bill Kilgore, Apocalypse Now');
INSERT INTO quotes(quote, author) VALUES ('Louis, I think this is the beginning of a beautiful friendship.', 'Rick Blaine, Casablanca' );
INSERT INTO quotes(quote, author) VALUES ('There''s no place like home.', 'Dorothy Gale, The Wizard of Oz');
INSERT INTO quotes(quote, author) VALUES ('Show me the money!', 'Rod Tidwell, Jerry Maguire');
INSERT INTO quotes(quote, author) VALUES ('You can''t handle the truth!', 'Col. Nathan Jessup, A Few Good Men' );

INSERT INTO quotes(quote, author) VALUES ('Wind up the usual suspects', 'Capt. Louis Renault, Casablanca');
INSERT INTO quotes(quote, author) VALUES ('I''ll have what she''s having', 'customer, When Harry Met Sally');
INSERT INTO quotes(quote, author) VALUES ('You''re gonna need a bigger boat.', 'Martin Brody, Jaws');
INSERT INTO quotes(quote, author) VALUES ('There''s no crying in baseball!', 'Jimmy Dugan, A League of Their Own');
INSERT INTO quotes(quote, author) VALUES ('Keep your friends close, but your enemies closer', 'Michael Corleone, The Godfather Part II');

INSERT INTO quotes(quote, author) VALUES ('We rob banks.', 'Clyde Barrow, Bonnie and Clyde');
INSERT INTO quotes(quote, author) VALUES ('I see dead people.', 'Cole Sear, The Sixth Sense' );
INSERT INTO quotes(quote, author) VALUES ('Houston, we have a problem.', 'Jim Lovell, Apollo 13' );
INSERT INTO quotes(quote, author) VALUES ('You had me at "hello."', 'Dorothy Boyd, Jerry Maguire');
INSERT INTO quotes(quote, author) VALUES ('A boy''s best friend is his mother.', 'Norman Bates, Psycho');
INSERT INTO quotes(quote, author) VALUES ('Greed, for lack of a better word, is good.', 'Gordon Gekko, Wall Street' );
INSERT INTO quotes(quote, author) VALUES ('As God is my witness, I''ll never be hungry again.', 'Scarlett O''Hara, Gone with the Wind');
INSERT INTO quotes(quote, author) VALUES ('Say hello to my little friend!', 'Tony Montana, Scarface' );

INSERT INTO quotes(quote, author) VALUES ('Elementary, my dear Watson.', 'Sherlock Holmes, The Adventures of Sherlock Holmes'); 
INSERT INTO quotes(quote, author) VALUES ('Get your stinking paws off me, you damned dirty ape.', 'George Taylor, Planet of the Apes');
INSERT INTO quotes(quote, author) VALUES ('Soylent Green is people!', 'Det. Robert Thorn, Soylent Green' );
INSERT INTO quotes(quote, author) VALUES ('Open the pod bay doors please, HAL.', 'Dave Bowman, 2001: A Space Odyssey' );
INSERT INTO quotes(quote, author) VALUES ('My precious.', 'Gollum, The Lord of the Rings: The Two Towers');
INSERT INTO quotes(quote, author) VALUES ('A martini. Shaken, not stirred.', 'James Bond, Goldfinger');
INSERT INTO quotes(quote, author) VALUES ('I feel the need — the need for speed!', 'Lt. Pete Mitchell & Lt. Nick Bradshaw, Top Gun' );
INSERT INTO quotes(quote, author) VALUES ('I''m the king of the world!', 'Jack Dawson, Titanic');


--movies
INSERT INTO quotes(quote, author) VALUES ('They may take our lives, but they''ll never take... OUR FREEDOM!', 'William wallace, Braveheart' );
INSERT INTO quotes(quote, author) VALUES ('Why so serious?', 'The Joker, The Dark Knight' );
INSERT INTO quotes(quote, author) VALUES ('Get off my plane!', 'President James Marshall, Air Force One' );
INSERT INTO quotes(quote, author) VALUES ('With great power comes great responsibility.', 'Uncle Ben, Spider Man' );
INSERT INTO quotes(quote, author) VALUES ('I find your lack of faith disturbing.', 'Darth Vader, Star Wars: Episode IV - A New Hope' );
INSERT INTO quotes(quote, author) VALUES ('It''s a trap!', 'Admiral Ackbar, Star Wars: Episode VI - Return of the Jedi' );
INSERT INTO quotes(quote, author) VALUES ('So this is how liberty dies... with thunderous applause.', 'Padme Amidala, Star Wars: Episode III - Revenge of the Sith' );
INSERT INTO quotes(quote, author) VALUES ('Never tell me the odds.', 'Han Solo, Star Wars: Episode V - The Empire Strikes Back' );
--INSERT INTO quotes(quote, author) VALUES ('Help me Obi-Wan Kenobi. You''re my only hope', 'Princess Leia' );
INSERT INTO quotes(quote, author) VALUES ('Well, what if there is no tomorrow? There wasn''t one today.', 'Groundhog Day' );

INSERT INTO quotes(quote, author) VALUES ('Germany has declared war on the Jones boys.', 'Walter Donovan, Indiana Jones and the Last Crusade' );
INSERT INTO quotes(quote, author) VALUES ('Truly wonderful the mind of a child is.', 'Yoda, Star Wars: Episode II - Attack of the Clones');
INSERT INTO quotes(quote, author) VALUES ('I have had it with these motherfucking snakes on this motherfucking plane!', 'Snakes on a Plane' );
INSERT INTO quotes(quote, author) VALUES ('Here''s another nice mess you''ve gotten me into! ', 'Sons of the Desert' );
INSERT INTO quotes(quote, author) VALUES ('I want to play a game...', 'Saw' );
INSERT INTO quotes(quote, author) VALUES ('I''ll have what she''s having.', 'When Harry Met Sally' );
INSERT INTO quotes(quote, author) VALUES ('It was beauty killed the beast.', 'King Kong' );
INSERT INTO quotes(quote, author) VALUES ('Let''s go to the Winchester, have a pint and wait for this to all blow over.', 'Shaun of the Dead' );
INSERT INTO quotes(quote, author) VALUES ('Man who catch fly with chopstick accomplish anything.', 'The Karate Kid' );
INSERT INTO quotes(quote, author) VALUES ('To call you stupid would be an insult to stupid people!', 'A Fish Called Wanda');

INSERT INTO quotes(quote, author) VALUES ('I just want to tell you both good luck. We''re all counting on you.', 'Dr. Rumack, Airplane');
INSERT INTO quotes(quote, author) VALUES ('You shall not pass!', 'Gandalf, The Fellowship of the Ring');


--taglines
INSERT INTO quotes(quote, author) VALUES ('In space no one can hear you scream.', 'Alien tagline' );
INSERT INTO quotes(quote, author) VALUES ('Earth. It was fun while it lasted.', 'Armageddon tagline' );
INSERT INTO quotes(quote, author) VALUES ('The true story of a real fake.', 'Catch Me If You Can tagline' );
INSERT INTO quotes(quote, author) VALUES ('His story will touch you, even though he can''t.', 'Edward Scissorhands tagline' );
INSERT INTO quotes(quote, author) VALUES ('She brought a small town to its feet and a huge corporation to its knees.', 'Erin Brockovich tagline' );
INSERT INTO quotes(quote, author) VALUES ('Be afraid. Be very afraid.', 'The Fly tagline' );
INSERT INTO quotes(quote, author) VALUES ('There can be only one.', 'Highlander tagline' );
INSERT INTO quotes(quote, author) VALUES ('Earth. Take a good look. It could be your last.', 'Independence day tagline' );
INSERT INTO quotes(quote, author) VALUES ('Reality is a thing of the past.', 'The Matrix tagline' );
INSERT INTO quotes(quote, author) VALUES ('Protecting the Earth from the scum of the universe!', 'Men in Black tagline' );

INSERT INTO quotes(quote, author) VALUES ('The first casualty of war is innocence.', 'Platoon tagline' );
INSERT INTO quotes(quote, author) VALUES ('The mission is a man.', 'Saving Private Ryan tagline' );
INSERT INTO quotes(quote, author) VALUES ('The thing that won''t die, in the nightmare that won''t end.', 'The Terminator tagline' );
INSERT INTO quotes(quote, author) VALUES ('You don''t get to 500 million friends without making a few enemies.', 'The Social Network tagline' );
INSERT INTO quotes(quote, author) VALUES ('Love is a force of nature.', 'Brokeback Mountain tagline' );
INSERT INTO quotes(quote, author) VALUES ('Everyone wants to be found.', 'Lost in Translation tagline' );
INSERT INTO quotes(quote, author) VALUES ('They''re young... they''re in love... and they kill people', 'Bonnie and Clyde tagline' );
INSERT INTO quotes(quote, author) VALUES ('On every street in every city, there''s a nobody who dreams of being a somebody.', 'Taxi Driver tagline' );
INSERT INTO quotes(quote, author) VALUES ('We had 20 years to prepare. So did they.', 'Independence Day: Resurgence tagline' );


--presidential campaign slogans
INSERT INTO quotes(quote, author) VALUES ('I Like Ike', 'Dwight D. Eisenhower presidential campaign -52' );
INSERT INTO quotes(quote, author) VALUES ('He''s Making Us Proud Again', 'Gerald Ford presidential campaign -76' );
INSERT INTO quotes(quote, author) VALUES ('It''s Morning Again in America', 'Ronald Reagan presidential campaign -84' );
INSERT INTO quotes(quote, author) VALUES ('Don''t stop thinking about tomorrow', 'Bill Clinton presidential campaign -92' );
INSERT INTO quotes(quote, author) VALUES ('America Needs a Change', 'Walter Mondale presidential campaign -84' );
INSERT INTO quotes(quote, author) VALUES ('The Better Man for a Better America', 'Bob Dole presidential campaign -96' );
INSERT INTO quotes(quote, author) VALUES ('Leave No Child Behind', 'George W. Bush presidential campaign -00' );
INSERT INTO quotes(quote, author) VALUES ('Let America Be America Again', 'John Kerry presidential campaign -04');
INSERT INTO quotes(quote, author) VALUES ('Change We Can Believe In', 'Barack Obama presidential campaign -08' );
INSERT INTO quotes(quote, author) VALUES ('Yes We Can!', 'Barack Obama presidential campaign -08' );


--company slogans
INSERT INTO quotes(quote, author) VALUES ('Think big.', 'Imax' );
INSERT INTO quotes(quote, author) VALUES ('Think different.', 'Apple' );
INSERT INTO quotes(quote, author) VALUES ('Between love and madness lies obsession.', 'Calvin Klein' );
INSERT INTO quotes(quote, author) VALUES ('Don''t be evil.', 'Google' );
INSERT INTO quotes(quote, author) VALUES ('Save Money. Live Better.', 'Walmart' );
INSERT INTO quotes(quote, author) VALUES ('When there is no tomorrow.', 'FedEx' );
INSERT INTO quotes(quote, author) VALUES ('The greatest tragedy is indifference.', 'Red Cross' );
INSERT INTO quotes(quote, author) VALUES ('The happiest place on earth.', 'Disneyland');
INSERT INTO quotes(quote, author) VALUES ('Impossible is nothing.', 'Adidas' );
INSERT INTO quotes(quote, author) VALUES ('A diamond is forever.', 'De Beers' );

INSERT INTO quotes(quote, author) VALUES ('Just do it.', 'Nike' );
INSERT INTO quotes(quote, author) VALUES ('Connecting people.', 'Nokia' );
INSERT INTO quotes(quote, author) VALUES ('Eat freash.', 'Subway' );
INSERT INTO quotes(quote, author) VALUES ('Challenge everything.', 'Electronic Arts' );
INSERT INTO quotes(quote, author) VALUES ('Your vision. Our future.', 'Olympus' );
INSERT INTO quotes(quote, author) VALUES ('Melts in your mouth, not in your hands.', 'M&M' );
INSERT INTO quotes(quote, author) VALUES ('Because you''re worth it.', 'L''Oreal' );
INSERT INTO quotes(quote, author) VALUES ('Imagination at work.', 'General Electric');
INSERT INTO quotes(quote, author) VALUES ('Miracles of science.', 'Du Pont' );
INSERT INTO quotes(quote, author) VALUES ('Don''t leave home without it.', 'American Express' );

INSERT INTO quotes(quote, author) VALUES ('The ultimate driving machine.', 'BMW' );
INSERT INTO quotes(quote, author) VALUES ('Probably the best beer in the world.', 'Carlsberg' );
INSERT INTO quotes(quote, author) VALUES ('Put a tiger in your tank.', 'Esso' );
INSERT INTO quotes(quote, author) VALUES ('Say it with flowers.', 'FTD' );
INSERT INTO quotes(quote, author) VALUES ('The Best a Man Can Get.', 'Gillette' );
INSERT INTO quotes(quote, author) VALUES ('All the news that''s fit to print.', 'The New York Times' );
INSERT INTO quotes(quote, author) VALUES ('Where''s the beef?', 'Wendy''s' );



--games
INSERT INTO quotes(quote, author) VALUES ('Thank you Mario! But our princess is in another castle!', 'Toad, Super Mario Bros.' );
INSERT INTO quotes(quote, author) VALUES ('The right man in the wrong place can make all the difference in the world.', 'G-Man, Half-Life 2' );
INSERT INTO quotes(quote, author) VALUES ('Why, that''s the second biggest monkey head I''ve ever seen!','Guybrush Threepwood, The Secret of Monkey Island' );
INSERT INTO quotes(quote, author) VALUES ('Is a man not entitled to the sweat of his brow?', 'Andrew Ryan, Bioshock' );
INSERT INTO quotes(quote, author) VALUES ('Jill, here''s a lockpick. It might come in handy if you, the master of unlocking, take it with you.', 'Barry Burton, Resident Evil' );
INSERT INTO quotes(quote, author) VALUES ('It''s dangerous to go alone; take this!', 'Old man, The Legend of Zelda' );
INSERT INTO quotes(quote, author) VALUES ('It''s super effective!', 'Pokemon' );
INSERT INTO quotes(quote, author) VALUES ('All your base are belong to us.', 'CATS, Zero Wing' );
INSERT INTO quotes(quote, author) VALUES ('Do a barrel roll!', 'Peppy, Star Fox' );
INSERT INTO quotes(quote, author) VALUES ('What is better: to be born good, or to overcome your evil nature through great effort?', 'Paarthurnax, Skyrim' );

INSERT INTO quotes(quote, author) VALUES ('Never pay more than 20 bucks for a computer game.', 'Guybrush Threepwood, The Secret of Monkey Island' );
INSERT INTO quotes(quote, author) VALUES ('Wake me when you need me.', 'Master Chief, Halo 3' );
INSERT INTO quotes(quote, author) VALUES ('In all things a calm heart must prevail.', 'Fawkes, Fallout 3' );
INSERT INTO quotes(quote, author) VALUES ('Cousin let''s go bowling.', 'Roman Bellic, Grand Theft Auto IV' );
INSERT INTO quotes(quote, author) VALUES ('Don''t make a girl a promise... if you know you can''t keep it.', 'Cortana, Halo 2' );
INSERT INTO quotes(quote, author) VALUES ('Prepare for unforeseen consequences.', 'G-Man, Half-Life 2' );
INSERT INTO quotes(quote, author) VALUES ('I''m Commander Shepard, and this my favorite store on the citadel!', 'Commander Shepard, Mass Effect 2' );
INSERT INTO quotes(quote, author) VALUES ('I used to be an adventurer like you, then I took an arrow in the knee.', 'Guard, Skyrim' );
INSERT INTO quotes(quote, author) VALUES ('Remember - no Russian', 'Vladimir Makarov, COD: Modern Warfare 2' );

INSERT INTO quotes(quote, author) VALUES ('Wake up Mr. Freeman, Wake up and smell the ashes.', 'G-Man, Half-Life 2' );


-- Duke Nukem
INSERT INTO quotes(quote, author) VALUES ('It''s time to kick ass and chew bubble gum... and I''m all outta gum.', 'Duke Nukem');
INSERT INTO quotes(quote, author) VALUES ('My name is Duke Nukem - and I''m coming to get the rest of you alien bastards!', 'Duke Nukem');
INSERT INTO quotes(quote, author) VALUES ('Nobody steals our chicks... and lives!', 'Duke Nukem');
INSERT INTO quotes(quote, author) VALUES ('Sometimes I even amaze myself.', 'Duke Nukem');
INSERT INTO quotes(quote, author) VALUES ('This''ll be a barrel of laughs.', 'Duke Nukem');


--Indiana Jones
INSERT INTO quotes(quote, author) VALUES ('Fortune and glory, kid. Fortune and glory.', 'Indiana Jones, Indiana Jones and the Temple of Doom');
INSERT INTO quotes(quote, author) VALUES ('Throw me the idol; I''ll throw you the whip!', 'Satipo, Raiders of the Lost Ark');
INSERT INTO quotes(quote, author) VALUES ('Nothing surprises me, I''m a scientist.', 'Indiana Jones, Indiana Jones and the Temple of Doom');
INSERT INTO quotes(quote, author) VALUES ('That belongs in a museum!', 'Indiana Jones, Indiana Jones and the Last Crusade');


--Civ 4
INSERT INTO quotes(quote, author) VALUES ('Do not throw the arrow which will return against you.', 'Kurdish Proverb');
INSERT INTO quotes(quote, author) VALUES ('Give a man a fish and you feed him for a day. Teach a man how to fish and you feed him for a lifetime.', 'Lao Tzu');
INSERT INTO quotes(quote, author) VALUES ('If you chase two rabbits, you will lose them both.', 'Native American proverb');
INSERT INTO quotes(quote, author) VALUES ('It is from their foes, not their friends, that cities learn the lesson of building high walls.', 'Aristophanes');
INSERT INTO quotes(quote, author) VALUES ('Meditation brings wisdom; lack of meditation leaves ignorance. Know well what leads you forward and what holds you back.', 'Buddha');
INSERT INTO quotes(quote, author) VALUES ('The man who moves a mountain begins by carrying away small stones.', 'Confucius');
INSERT INTO quotes(quote, author) VALUES ('The wisest men follow their own direction.', 'Euripides');
INSERT INTO quotes(quote, author) VALUES ('You should hammer your iron when it is glowing hot.', 'Publius Syrus');
INSERT INTO quotes(quote, author) VALUES ('Some books are to be tasted, others to be swallowed, and some to be chewed and digested.', 'Sir Francis Bacon');
INSERT INTO quotes(quote, author) VALUES ('A multitude of rulers is not a good thing. Let there be one ruler, one king.', 'Herodotus');

INSERT INTO quotes(quote, author) VALUES ('Banking establishments are more dangerous than standing armies.', 'Thomas Jefferson');
INSERT INTO quotes(quote, author) VALUES ('I am the state.', 'Louis XIV');
INSERT INTO quotes(quote, author) VALUES ('I will to my lord be true and faithful, and love all which he loves and shun all which he shuns.', 'Anglo Saxon oath of Fealty');
INSERT INTO quotes(quote, author) VALUES ('No freeman shall be taken, imprisoned, or in any other way destroyed, except by the lawful judgment of his peers.', 'Magna Carta');
INSERT INTO quotes(quote, author) VALUES ('Everything we hear is an opinion, not a fact. Everything we see is a perspective, not the truth.', 'Marcus Aurelius');
INSERT INTO quotes(quote, author) VALUES ('Any society that would give up a little liberty to gain a little security will deserve neither and lose both.', 'Benjamin Franklin');
INSERT INTO quotes(quote, author) VALUES ('I must study politics and war that my sons may have liberty to study mathematics and philisophy.', 'John Adams');
INSERT INTO quotes(quote, author) VALUES ('What gunpowder did for war, the printing press has done for the mind.', 'Wendell Phillips');
INSERT INTO quotes(quote, author) VALUES ('The whole is more than the sum of its parts.', 'Aristotle');

INSERT INTO quotes(quote, author) VALUES ('It is not the strongest of the species that survive, but the one most responsive to change.', 'Charles Darwin');
INSERT INTO quotes(quote, author) VALUES ('Everything in life is somewhere else, and you get there in a car.', 'E.B. White');
INSERT INTO quotes(quote, author) VALUES ('When I give food to the poor, they call me a saint. When I ask why the poor have no food, they call me a communist.', 'Dom Helder Camara');
INSERT INTO quotes(quote, author) VALUES ('To every action there is always opposed an equal reaction.', 'Isaac Newton');
INSERT INTO quotes(quote, author) VALUES ('It has been said that democracy is the worst form of government except all the others that have been tried.', 'Winston Churchill');
INSERT INTO quotes(quote, author) VALUES ('Compound interest is the most powerful force in the universe.', 'Albert Einstein');
INSERT INTO quotes(quote, author) VALUES ('Never trust a computer you can''t throw out a window.', 'Steve Wozniak');
INSERT INTO quotes(quote, author) VALUES ('The future will be better tomorrow.', 'Dan Quayle');
INSERT INTO quotes(quote, author) VALUES ('Any sufficiently advanced technology is indistinguishable from magic.', 'Arthur C. Clarke');
INSERT INTO quotes(quote, author) VALUES ('Tell me what you eat, and I will tell you what you are.', 'Anthelme Brillat-Savarin');
INSERT INTO quotes(quote, author) VALUES ('What is happiness? The feeling that power is growing, that resistance is overcome.', 'Friedrich Nietzsche');

--civ5
INSERT INTO quotes(quote, author) VALUES ('Once the rockets are up, who cares where they come down?', 'Tom Lehrer');
INSERT INTO quotes(quote, author) VALUES ('Where tillage begins, other arts follow. The farmers therefore are the founders of human civilization.', 'Daniel Webster');
INSERT INTO quotes(quote, author) VALUES ('Those who cannot remember the past are condemned to repeat it.', 'George Santayana');
INSERT INTO quotes(quote, author) VALUES ('Happiness: a good bank account, a good cook and a good digestion.', 'Jean Jacques Rousseau');
INSERT INTO quotes(quote, author) VALUES ('If the brain were so simple we could understand it, we would be so simple we couldn''t.', 'Lyall Watson');
INSERT INTO quotes(quote, author) VALUES ('The only thing that saves us from the bureaucracy is its inefficiency.', 'Eugene McCarthy');
INSERT INTO quotes(quote, author) VALUES ('Any man who can drive safely while kissing a pretty girl is simply not giving the kiss the attention it deserves.', 'Albert Einstein');
INSERT INTO quotes(quote, author) VALUES ('I find the great thing in this world is not so much where we stand, as in what direction we are moving.', 'Oliver Wendell Holmes');
INSERT INTO quotes(quote, author) VALUES ('Better is bread with a happy heart than wealth with vexation.', 'Amenemope');
INSERT INTO quotes(quote, author) VALUES ('Education is the best provision for old age.', 'Aristotle');

INSERT INTO quotes(quote, author) VALUES ('There''s a basic principle about consumer electronics: it gets more powerful all the time and it gets cheaper all the time.', 'Trip Hawkins');
INSERT INTO quotes(quote, author) VALUES ('Instrumental or mechanical science is the noblest and, above all others, the most useful.', 'Leonardo da Vinci');
INSERT INTO quotes(quote, author) VALUES ('Aeronautics was neither an industry nor a science. It was a miracle.', 'Igor Sikorsky');
INSERT INTO quotes(quote, author) VALUES ('I think we all agree, the past is over.', 'George W. Bush');
INSERT INTO quotes(quote, author) VALUES ('The new electronic interdependence recreates the world in the image of a global village.', 'Marshall McLuhan');
INSERT INTO quotes(quote, author) VALUES ('Do not wait to strike until the iron is hot; but make it hot by striking.', 'William Butler Yeats');
INSERT INTO quotes(quote, author) VALUES ('How happy are those whose walls already rise!', 'Virgil');
INSERT INTO quotes(quote, author) VALUES ('Mathematics is the gate and key to the sciences.', 'Roger Bacon');
INSERT INTO quotes(quote, author) VALUES ('There never was a good knife made of bad steel.', 'Benjamin Franklin');

INSERT INTO quotes(quote, author) VALUES ('The meek shall inherit the Earth, but not its mineral rights.', 'J. Paul Getty');
INSERT INTO quotes(quote, author) VALUES ('The impact of nanotechnology is expected to exceed the impact the electronics revolution has had on our lives.', 'Richard Schwartz');
INSERT INTO quotes(quote, author) VALUES ('The nation that destroys its soil destroys itself.', 'Franklin D. Roosevelt');
INSERT INTO quotes(quote, author) VALUES ('The winds and the waves are always on the side of the ablest navigators.', 'Edward Gibbon');
INSERT INTO quotes(quote, author) VALUES ('I am become Death, the destroyer of worlds.', 'Robert Oppenheimer');
INSERT INTO quotes(quote, author) VALUES ('There is only one good, knowledge, and one evil, ignorance.', 'Socrates');
INSERT INTO quotes(quote, author) VALUES ('Measure what is measurable, and make measurable what is not so.', 'Galileo');
INSERT INTO quotes(quote, author) VALUES ('It is a newspaper''s duty to print the news and raise hell.', 'The Chicago Times');
INSERT INTO quotes(quote, author) VALUES ('Vision is the art of seeing things invisible.', 'Jonathan Swift');
INSERT INTO quotes(quote, author) VALUES ('The whole country was tied together by radio. We all experienced the same heroes and comedians and singers. They were giants.', 'Woody Allen');

INSERT INTO quotes(quote, author) VALUES ('Nothing is particularly hard if you divide it into small jobs.', 'Henry Ford');
INSERT INTO quotes(quote, author) VALUES ('A robot may not injure a human being or, through inaction, allow a human being to come to harm.', '1st Law of Robotics');
INSERT INTO quotes(quote, author) VALUES ('A robot must obey any orders given to it by human beings, except where such orders would conflict with the First Law.', '2nd Law of Robotics');
INSERT INTO quotes(quote, author) VALUES ('A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.', '3rd Law of Robotics');
INSERT INTO quotes(quote, author) VALUES ('A good rule for rocket experimenters to follow is this: always assume that it will explode.', 'Astronautics Magazine, 1937');
INSERT INTO quotes(quote, author) VALUES ('He who commands the sea has command of everything.', 'Themistocles');
INSERT INTO quotes(quote, author) VALUES ('Now, somehow, in some new way, the sky seemed almost alien.', 'Lyndon B. Johnson');
INSERT INTO quotes(quote, author) VALUES ('Every great advance in science has issues from a new audacity of imagination.', 'John Dewey');
INSERT INTO quotes(quote, author) VALUES ('I once sent a dozen of my friends a telegram saying "flee at once - all is discovered." They all left town immediately.', 'Mark Twain');

INSERT INTO quotes(quote, author) VALUES ('Even brute beasts and wandering birds do not fall for the same traps or nets twice.', 'Saint Jerome');
INSERT INTO quotes(quote, author) VALUES ('He who destroys a good book kills reason itself.', 'John Milton');
INSERT INTO quotes(quote, author) VALUES ('To achieve great things, two things are needed: a plan, and not quite enough time.', 'Leonard Bernstein');
INSERT INTO quotes(quote, author) VALUES ('We only live to discover beauty. All else is a form of waiting.', 'Kahlil Gibran');
INSERT INTO quotes(quote, author) VALUES ('Every genuine work of art has as much reason for being as the earth and the sun.', 'Ralph Waldo Emerson');
INSERT INTO quotes(quote, author) VALUES ('In preparing for battle I have always found that plans are useless, but planning is indispensable.', 'Dwight D. Eisenhower');
INSERT INTO quotes(quote, author) VALUES ('Time crumbles things; everything grows old and is forgotten under the power of time.', 'Aristotle');
INSERT INTO quotes(quote, author) VALUES ('Those who lose dreaming are lost.', 'Australian Aboriginal saying');
INSERT INTO quotes(quote, author) VALUES ('The nations of the West hope that by means of steam communications all the world will become as one family.', 'Townsend Harris');
INSERT INTO quotes(quote, author) VALUES ('The absurd is the essential concept and the first truth.', 'Albert Camus');

INSERT INTO quotes(quote, author) VALUES ('The brain is like a muscle. When it is in use we feel very good. Understanding is joyous.', 'Carl Sagan');
INSERT INTO quotes(quote, author) VALUES ('The physician can bury his mistakes, but the architect can only advise his client to plant vines.', 'Frank Lloyd Wright');
INSERT INTO quotes(quote, author) VALUES ('Numberless are the world''s wonders, but none more wonderful than man.', 'Sophocles');
INSERT INTO quotes(quote, author) VALUES ('Honesty is the best policy.', 'Miguel de Cervantes');
INSERT INTO quotes(quote, author) VALUES ('He who knows others is wise; He who know himself is enlightened.', 'Lao Tzu');
INSERT INTO quotes(quote, author) VALUES ('The day of small nations has long passed away. The day of empires has come.', 'Joseph Chamberlain');
INSERT INTO quotes(quote, author) VALUES ('The future is not what it used to be.', 'Yogi Berra');


--facts
--http://www.thefactsite.com/2011/07/top-100-random-funny-facts.html
--http://www.cs.cmu.edu/~bingbin/
--https://www.reddit.com/r/funfacts/
INSERT INTO quotes(quote, author) VALUES ('Banging your head against a wall burns 150 calories an hour.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('In the UK, it is illegal to eat mince pies on Christmas Day!', 'fact');
INSERT INTO quotes(quote, author) VALUES ('When hippos are upset, their sweat turns red.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('A flock of crows is known as a murder.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('During your lifetime, you will produce enough saliva to fill two swimming pools.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('An eagle can kill a young deer and fly away with it.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Bikinis and tampons invented by men.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('A toaster uses almost half as much energy as a full-sized oven.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('You cannot snore and dream at the same time.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('A baby octopus is about the size of a flea when it is born.', 'fact');

INSERT INTO quotes(quote, author) VALUES ('Nearly three percent of the ice in Antarctic glaciers is penguin urine.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('A small child could swim through the veins of a blue whale.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The total number of steps in the Eiffel Tower are 1665.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Pirates wore earrings because they believed it improved their eyesight.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The testicles on an octopus are located in its head!', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Birds don''t urinate.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('An apple, potato, and onion all taste the same if you eat them with your nose plugged.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The average person walks the equivalent of twice around the world in a lifetime.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The inventor of the Waffle Iron did not like waffles.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Hares are born with fur and can see whilst rabbits are born naked and blind.', 'fact');

INSERT INTO quotes(quote, author) VALUES ('When you die your hair still grows for a couple of months.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The Neanderthal''s brain was bigger than yours is.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The pancreas produces insulin.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Elephants are the only mammals that can''t jump.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('If you had enough water to fill one million goldfish bowls, you could fill an entire stadium.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Cats can hear ultrasound.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Children grow faster in the springtime.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('When a male penguin falls in love with female penguin, he searches the entire beach to find the perfect pebble to present to her.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('A bolt of lightning is six times hotter than the sun.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Walt Disney had a phobia of mice.', 'fact');

INSERT INTO quotes(quote, author) VALUES ('Some tumors can grow hair, bones and teeth.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Only 2% of Earth population naturally has green eyes.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Crying makes you feel better, reduce stress, and may help to keep the body healthy.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('All pandas in the world are on loan from China.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('At room temperature, the average air molecule travels at the speed of a rifle bullet.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Dolphins recognize and admire themselves in mirrors.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('An ant’s sense of smell is stronger than a dog’s.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('A snail breathes through its foot.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Honeybees navigate by using the sun as a compass.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Banana milkshake is the perfect cure for hangover.', 'fact');

INSERT INTO quotes(quote, author) VALUES ('Goldfish don’t have stomachs.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Taking a quick nap after learning can help strengthen your memory.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Cherries can cause cancer cells to kill themselves.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Smiling actually boosts your immune system.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Dogs and elephants are the only animals that understand pointing.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Lemons are more acidic than vinegar.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Almost a third of the worlds languages are spoken only in Africa.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('You can start a fire with ice.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The oil in cashews helps prevent tooth decay.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The sun evaporates about a trillion tons of water a day.', 'fact');

INSERT INTO quotes(quote, author) VALUES ('Shrimp can only swim backwards.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Broccoli is the only vegetable that is also a flower.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Antarctica is the only continent with no owls.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('A cat’s lower jaw cannot move sideways.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Squirrels lose more than half of the nuts they hide.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('As we continue to evolve, scientists believe that fewer and fewer humans will be born with wisdom teeth.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Karoke means "empty orchestra" in Japanese.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The king of hearts is the only king without a moustache.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('It is genetically impossible for a rose to come in color blue. ', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The elephant is the only animal with 4 knees.', 'fact');

INSERT INTO quotes(quote, author) VALUES ('The Romans used to make toothpaste from urine.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Catfish are the only animals that naturally have an odd number of whiskers.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Most lipstick contains fish scales.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('12 newborns will be given to the wrong parents daily.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The microwave was invented after a researcher walked by a radar tube and a chocolate bar melted in his pocket.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('It''s impossible to lick your elbow.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Human thigh bones are stronger than concrete.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Eating lemons makes you live longer.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Soldiers from every country salute with their right hand. ', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Scientists can make teeth out of pee.', 'fact');

INSERT INTO quotes(quote, author) VALUES ('The distance from the Earth to the Moon is approximately 109 Moons.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('A honeybee''s true surface area is the size of a piece of toast.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('A manatee''s nipples are in its armpits.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Violent dreams may be an early sign of brain disorders down the line, including Parkinson''s disease and dementia.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The average keyboard contains 3,295 microbes per square inch.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Road traffic accidents kill more people around the world than malaria.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Cannibalism is legal in the U.S.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Kissing a baby on the ear can make it go deaf because of a condition known as "cochlear ear-kiss injury."', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Astronauts aboard Apollo 10 heard unexplained "outer spacey" music while orbiting the dark side of the moon.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Lying flat on your back is your best bet for surviving a falling elevator.', 'fact');

INSERT INTO quotes(quote, author) VALUES ('People with Cotard Syndrome believe they are dead or have lost their internal organs.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Snakes kill 100,000 people every year.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('It is estimated that 1% of society are psychopaths.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('There are more guns than people in the United States.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Bananas Are Radioactive.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The bubbles in champagne are, essentially, yeast farts.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('There are more hydrogen atoms in a teaspoon of water than there are teaspoons of water in the sea.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The word bed actually looks like a bed.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('All of the planets could fit inbetween the earth and the moon.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('The were still mammoths roaming the earth by the time the pyramids were being constructed.', 'fact');

INSERT INTO quotes(quote, author) VALUES ('Seahorses are raised by their fathers.', 'fact');
INSERT INTO quotes(quote, author) VALUES ('Mitochondria is the powerhouse of the cell.', 'fact');



--lyrics
INSERT INTO quotes(quote, author) VALUES ('In the end, the love you take is equal to the love you make.', 'The Beatles');
INSERT INTO quotes(quote, author) VALUES ('All you need is love.', 'The Beatles');






-- The lyrics table.
-- The status column in the first row denotes the next line to read next.
-- status: 1 -- first line of a new song
DROP TABLE IF EXISTS lyrics;
CREATE TABLE lyrics (title TEXT, search TEXT UNIQUE, verse TEXT, status INTEGER);


--status row
INSERT INTO lyrics(status) VALUES (2);

--Californication
INSERT INTO lyrics(title, search, verse, status) VALUES ('Red Hot Chili Peppers - Californication','Californication', 'Psychic spies from China try to steal your mind''s elation', 1);
INSERT INTO lyrics(verse) VALUES ('Little girls from Sweden dream of silver screen quotations');
INSERT INTO lyrics(verse) VALUES ('And if you want these kind of dreams it''s Californication');
INSERT INTO lyrics(verse) VALUES ('It''s the edge of the world and all of western civilization');
INSERT INTO lyrics(verse) VALUES ('The sun may rise in the East at least it settles in the final location');
INSERT INTO lyrics(verse) VALUES ('It''s understood that Hollywood sells Californication');
INSERT INTO lyrics(verse) VALUES ('Pay your surgeon very well to break the spell of aging');
INSERT INTO lyrics(verse) VALUES ('Celebrity skin is this your chin or is that war your waging');
INSERT INTO lyrics(verse) VALUES ('First born unicorn hard core soft porn');
INSERT INTO lyrics(verse) VALUES ('Dream of Californication, dream of Californication');
INSERT INTO lyrics(verse) VALUES ('Marry me girl be my fairy to the world be my very own constellation');
INSERT INTO lyrics(verse) VALUES ('A teenage bride with a baby inside getting high on information');

INSERT INTO lyrics(verse) VALUES ('And buy me a star on the boulevard it''s Californication');
INSERT INTO lyrics(verse) VALUES ('Space may be the final frontier but it''s made in a Hollywood basement');
INSERT INTO lyrics(verse) VALUES ('Cobain can you hear the spheres singing songs off station to station');
INSERT INTO lyrics(verse) VALUES ('And Alderon''s not far away it''s Californication');
INSERT INTO lyrics(verse) VALUES ('Born and raised by those who praise control of population everybody''s been there and I don''t mean on vacation');
INSERT INTO lyrics(verse) VALUES ('Destruction leads to a very rough road but it also breeds creation');
INSERT INTO lyrics(verse) VALUES ('And earthquakes are to a girl''s guitar they''re just another good vibration');

INSERT INTO lyrics(verse) VALUES ('And tidal waves couldn''t save the world from Californication');
INSERT INTO lyrics(verse) VALUES ('Pay your surgeon very well to break the spell of aging');
INSERT INTO lyrics(verse) VALUES ('Sicker than the rest there is no test but this is what you''re craving');

--Stairway to Heaven
INSERT INTO lyrics(title, search, verse, status) VALUES ('Led Zeppelin - Stairway to Heaven', 'Stairway to Heaven', 'There''s a lady who''s sure all that glitters is gold', 1);
INSERT INTO lyrics(verse) VALUES ('And she''s buying a stairway to heaven. When she gets there she knows, if the stores are all closed');
INSERT INTO lyrics(verse) VALUES ('With a word she can get what she came for. And she''s buying a stairway to heaven.');
INSERT INTO lyrics(verse) VALUES ('There''s a sign on the wall but she wants to be sure');
INSERT INTO lyrics(verse) VALUES ('Cause you know sometimes words have two meanings.');
INSERT INTO lyrics(verse) VALUES ('In a tree by the brook, there''s a songbird who sings, sometimes all of our thoughts are misgiven.');
INSERT INTO lyrics(verse) VALUES ('Ooh, it makes me wonder, ooh, it makes me wonder.');
INSERT INTO lyrics(verse) VALUES ('There''s a feeling I get when I look to the west, and my spirit is crying for leaving.');
INSERT INTO lyrics(verse) VALUES ('In my thoughts I have seen rings of smoke through the trees, and the voices of those who stand looking.');
INSERT INTO lyrics(verse) VALUES ('Ooh, it makes me wonder, ooh, it really makes me wonder.');
INSERT INTO lyrics(verse) VALUES ('And it''s whispered that soon, if we all call the tune, then the piper will lead us to reason.');
INSERT INTO lyrics(verse) VALUES ('And a new day will dawn for those who stand long, and the forests will echo with laughter.');

INSERT INTO lyrics(verse) VALUES ('If there''s a bustle in your hedgerow, don''t be alarmed now, it''s just a spring clean for the May queen.');
INSERT INTO lyrics(verse) VALUES ('Yes, there are two paths you can go by, but in the long run');
INSERT INTO lyrics(verse) VALUES ('There''s still time to change the road you''re on. And it makes me wonder.');
INSERT INTO lyrics(verse) VALUES ('Your head is humming and it won''t go, in case you don''t know, the piper''s calling you to join him,');
INSERT INTO lyrics(verse) VALUES ('Dear lady, can you hear the wind blow, and did you know your stairway lies on the whispering wind?');
INSERT INTO lyrics(verse) VALUES ('And as we wind on down the road our shadows taller than our soul.');
INSERT INTO lyrics(verse) VALUES ('There walks a lady we all know who shines white light and wants to show');

INSERT INTO lyrics(verse) VALUES ('How everything still turns to gold. And if you listen very hard');
INSERT INTO lyrics(verse) VALUES ('The tune will come to you at last. When all are one and one is all');
INSERT INTO lyrics(verse) VALUES ('To be a rock and not to roll. And she''s buying a stairway to heaven.');

--How Can I Tell You?
INSERT INTO lyrics(title, search, verse, status) VALUES ('Cat Stevens - How Can I Tell You?', 'How Can I Tell You?', 'How can I tell you that I love you, I love you', 1);
INSERT INTO lyrics(verse) VALUES ('But I can''t think of right words to say, I long to tell you that I''m always thinking of you');
INSERT INTO lyrics(verse) VALUES ('I''m always thinking of you, but my words just blow away, just blow away');
INSERT INTO lyrics(verse) VALUES ('It always ends up to one thing, honey and I can''t think of right words to say');
INSERT INTO lyrics(verse) VALUES ('Wherever I am girl, I''m always walking with you I''m always walking with you, but I look and you''re not there');
INSERT INTO lyrics(verse) VALUES ('Whoever I''m with, I''m always, always talking to you I''m always talking to you, and I''m sad that');
INSERT INTO lyrics(verse) VALUES ('You can''t hear, sad that you can''t hear it always ends up to one thing, honey,');
INSERT INTO lyrics(verse) VALUES ('When I look and you''re not there I need to know you, need to feel my arms around you');
INSERT INTO lyrics(verse) VALUES ('Feel my arms around you, like a sea around a shore and each night and day I pray, in hope');
INSERT INTO lyrics(verse) VALUES ('That I might find you, in hope that I might find you, because heart''s can do no more');
INSERT INTO lyrics(verse) VALUES ('It always ends up to one thing honey, still I kneel upon the floor how can I tell you that I love you, I love you');
INSERT INTO lyrics(verse) VALUES ('But I can''t think of right words to say I long to tell you that I''m always thinking of you');
INSERT INTO lyrics(verse) VALUES ('I''m always thinking of you... It always ends up to one thing honey and I can''t think of right words to say');

--The Zen of Python
INSERT INTO lyrics(title, search, verse, status) VALUES ('The Zen of Python', 'The Zen of Python', 'Beatiful is better than ugly.', 1);
INSERT INTO lyrics(verse) VALUES ('Explicit is better than implicit.');
INSERT INTO lyrics(verse) VALUES ('Simple is better than complex.' );
INSERT INTO lyrics(verse) VALUES ('complex is better than complicated.' );
INSERT INTO lyrics(verse) VALUES ('Flat is better than nested.' );
INSERT INTO lyrics(verse) VALUES ('Sparse is better than dense.' );
INSERT INTO lyrics(verse) VALUES ('Readability counts.' );
INSERT INTO lyrics(verse) VALUES ('Special cases aren''t special enough to break the rules.' );
INSERT INTO lyrics(verse) VALUES ('Although practicality beats purity.' );
INSERT INTO lyrics(verse) VALUES ('Errors should never pass silently.' );
INSERT INTO lyrics(verse) VALUES ('Unless explicitly silenced.' );
INSERT INTO lyrics(verse) VALUES ('In the face of ambiguity, refuse the temptation to guess.');
INSERT INTO lyrics(verse) VALUES ('There should be one, and preferably only one, obvious way to do it.' );
INSERT INTO lyrics(verse) VALUES ('Although that way may not be obvious at first unless you''re Dutch.');
INSERT INTO lyrics(verse) VALUES ('Now is better than never.' );
INSERT INTO lyrics(verse) VALUES ('Although never is often better than right now.' );
INSERT INTO lyrics(verse) VALUES ('If the implementation is hard to explain, it''s a bad idea.' );
INSERT INTO lyrics(verse) VALUES ('If the implementation is easy to explain, it may be a good idea.' );
INSERT INTO lyrics(verse) VALUES ('Namespaces are one honking great idea - let''s do more of those!');

--Nights in white satin
INSERT INTO lyrics(title, search, verse, status) VALUES ('Moody Blues - Nights in White Satin', 'Nights in White Satin', 'Nights in white satin', 1);
INSERT INTO lyrics(verse) VALUES ('Never reaching the end. Letters I''ve written never meaning to send.');
INSERT INTO lyrics(verse) VALUES ('Beauty I''ve always missed With these eyes before.' );
INSERT INTO lyrics(verse) VALUES ('Just what the truth is I can''t say any more.' );
INSERT INTO lyrics(verse) VALUES ('Cause I love you, yes I love you. Oh how I love you.' );
INSERT INTO lyrics(verse) VALUES ('Gazing at people some hand in hand just what I''m going through they can''t understand.' );
INSERT INTO lyrics(verse) VALUES ('Some try to tell me thoughts they cannot defend. Just what you want to be you will be in the end.' );
INSERT INTO lyrics(verse) VALUES ('And I love you, yes I love you.' );
INSERT INTO lyrics(verse) VALUES ('Oh how I love you, oh how I love you.' );
INSERT INTO lyrics(verse) VALUES ('Nights in white satin never reaching the end.' );
INSERT INTO lyrics(verse) VALUES ('Letters I''ve written never meaning to send.' );
INSERT INTO lyrics(verse) VALUES ('Beauty I''ve always missed With these eyes before.');
INSERT INTO lyrics(verse) VALUES ('Just what the truth is I can''t say any more.' );
INSERT INTO lyrics(verse) VALUES ('Cause I love you, yes I love you. Oh how I love you, oh how I love you.');

--What a Wonderful World
INSERT INTO lyrics(title, search, verse, status) VALUES ('Louis Armstrong - What a Wonderful World', 'What a Wonderful World', 'I see trees of green, red roses too.', 1);
INSERT INTO lyrics(verse) VALUES ('I see them bloom for me and you and I think to myself what a wonderful world.' );
INSERT INTO lyrics(verse) VALUES ('I see skies of blue and clouds of white. The bright blessed day, the dark sacred night.' );
INSERT INTO lyrics(verse) VALUES ('And I think to myself what a wonderful world.' );
INSERT INTO lyrics(verse) VALUES ('The colors of the rainbow so pretty in the sky, are also on the faces of people going by.' );
INSERT INTO lyrics(verse) VALUES ('I see friends shaking hands saying how do you do, but they''re really saying I love you.' );
INSERT INTO lyrics(verse) VALUES ('I hear baby''s crying and I watched them grow, they''ll learn much more than I''ll ever know.' );
INSERT INTO lyrics(verse) VALUES ('And I think to myself what a wonderful world. Yes, I think to myself what a wonderful world.');

--Behind Blue Eyes
INSERT INTO lyrics(title, search, verse, status) VALUES ('Limp Bizkit - Behind Blue Eyes', 'Behind Blue Eyes', 'No one knows what it''s like to be the bad man, to be the sad man. Behind blue eyes.', 1);
INSERT INTO lyrics(verse) VALUES ('And no one knows what it''s like to be hated, to be fated to telling only lies.' );
INSERT INTO lyrics(verse) VALUES ('But my dreams they aren''t as empty as my conscience seems to be.' );
INSERT INTO lyrics(verse) VALUES ('I have hours, only lonely. My love is vengeance that''s never free.' );
INSERT INTO lyrics(verse) VALUES ('No one knows what its like to feel these feelings like I do, and I blame you!' );
INSERT INTO lyrics(verse) VALUES ('No one bites back as hard on their anger.' );
INSERT INTO lyrics(verse) VALUES ('None of my pain and woe can show through.' );
INSERT INTO lyrics(verse) VALUES ('No one knows what its like to be mistreated, to be defeated behind blue eyes.' );
INSERT INTO lyrics(verse) VALUES ('No one knows how to say that they''re sorry and don''t worry. I''m not telling lies.' );
INSERT INTO lyrics(verse) VALUES ('No one knows what its like to be the bad man, to be the sad man. Behind blue eyes.');

--Yesterday
INSERT INTO lyrics(title, search, verse, status) VALUES ('The Beatles - Yesterday', 'Yesterday', 'Yesterday all my troubles seemed so far away.', 1);
INSERT INTO lyrics(verse) VALUES ('Now it looks as though they''re here to stay. Oh, I believe in yesterday.' );
INSERT INTO lyrics(verse) VALUES ('Suddenly I''m not half the man I used to be. There''s a shadow hanging over me. Oh, yesterday came suddenly.' );
INSERT INTO lyrics(verse) VALUES ('Why she had to go, I don''t know, she wouldn''t say. I said something wrong, now I long for yesterday.' );
INSERT INTO lyrics(verse) VALUES ('Yesterday love was such an easy game to play. Now I need a place to hide away. Oh, I believe in yesterday.' );
INSERT INTO lyrics(verse) VALUES ('Why she had to go, I don''t know, she wouldn''t say. I said something wrong, now I long for yesterday.' );
INSERT INTO lyrics(verse) VALUES ('Yesterday love was such an easy game to play.' );
INSERT INTO lyrics(verse) VALUES ('Now I need a place to hide away. Oh, I believe in yesterday.');
