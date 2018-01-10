var mongoose = require('mongoose');

var MongooseSchema = new mongoose.Schema({
    name:{
        type: String,
    },
    height:{
        type: String,
    },
    weight:{
        type: String,
    },
    color:{
        type: String,
    },
    description:{
        type: String,
    }
})

mongoose.model('Mongoose', MongooseSchema);