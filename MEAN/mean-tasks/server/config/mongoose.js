const mongoose = require('mongoose');
const fs = require('fs');
const path = require('path');
const DBNAME = 'task-mean-demon';

mongoose.Promise = global.Promise;

mongoose.connect('mongodb:localhost/${DBNAME}', () => console.log('connected to the ${DBNAME) database'))

//Import all of the models

const models_path = path.resolve(__dirname, '..', 'models')

fs.readdirSync(models_path).forEach(function(file) {
    if(file.indexOf('.js') >= 0) {
      require(models_path + '/' + file);
    }
});