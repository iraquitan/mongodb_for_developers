/**
 * Created by Iraquitan Cordeiro Filho on 8/29/16.
 */
use blog;

// index for sorting posts with decreasing date
db.posts.createIndexes({date: -1});

// index for finding posts by permalink
db.posts.createIndexes({permalink: 1});

// index for finding posts by tag with decreasing date
db.posts.createIndexes({tags: 1, date: -1});
