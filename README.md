# Monster Hunter App

![mh](https://user-images.githubusercontent.com/75986085/146096718-9803459f-210a-42b0-9d21-4759f12a242c.png)


<h2>1. Business Problem (Objectives)</h2>
<hr>

<p>Some data with information of monster hunter freedom unite game on wiki page or other websites. All information must be easily accessed by the user, you is free to select what of visual product of the data.</p>
 <ul>
    <li>All Quests.</li>
    <li>All Monster.</li>
    <li>All Items.</li>
    <li>Mix Sets Gunner & Blademaster.</li>
</ul>

<h2>2. Solution Strategy & Assumptions</h2>
<hr>

<p>This app is a visual product result of web scraping in a monster hunter freedom unite game webpage.</p>

![app](https://user-images.githubusercontent.com/75986085/165653432-45248937-9727-4a9a-a434-f1c19fa2aa6f.png)


<h3>2.1. Assumptions</h3>
<p>The game never get new updates and easy to get data, but some of this data haved a last update on 2012, having some inconsistents.</p>

<h3>2.2. First CRISP Cycle</h3>
<ul>
  <dl>
    <dt>Visual Product Design.</dt>
      <dd>The first step is to define the visual product, after some design ideas in paint between streamlit and pysimplegui, I opted for pysimplegui to use it more often.</dd>
    <dt>Data Collect.</dt>
      <dd>Used jp and en wiki of monster hunter freedom unite.</dd>
    <dt>Data Cleaning.</dt>
      <dd>Simple regex applications and pandas manipulation using wiki and real game to fill some na or inconsistent values.</dd>
    <dt>Data Storing.</dt>
      <dd>Only on CSV files fot app.</dd>
  </dl>
</ul>

<h3>2.3. Second CRISP Cycle</h3>
<p>In this step I have Build the MixSets Layout and created some Mix Sets on App with Another python Class to store the Mix Sets Information.</p>

<ul>
  <dl>
    <dt>Mix Armors Sets.</dt>
      <dd>Actually working on Mix Sets Armors.</dd>
  </dl>
</ul>

<h2>3. Data Granularity</h2>
<hr>

<h3>Item Data </h3>
<ul>
  <li>Item Name Granularity.</li>
</ul>
<h3>Quests Data </h3>
<ul>
  <li>Hunter Rank Granularity.</li>
</ul>
<h3>Monster Data </h3>
<ul>
  <li>Monster Name Granularity.</li>
</ul>

<h2>4. Mix Sets Armor Building</h2>
<hr>

<p>The step of getting images with (269x400) px is very tedious because i need to open my game, print the game scene and cut img on Paint xD.</p>

![test_mix_armor](https://user-images.githubusercontent.com/75986085/165651884-9a56cb2e-b5c4-4082-a58b-26401dfbe98d.png)

<h2>5. Little Problems Finded</h2>
<p>Some missing data and different tables sizes on wiki.</p>
