var express = require('express');
var session = require('express-session');
var bodyParser = require('body-parser');
var path = require('path');
var mongoose = require('mongoose');

var app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, './static')));
app.use(session({secret: 'codingdojorocks'}));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

mongoose.connect('mongodb://localhost/basic_mongoose');
mongoose.Promise = global.Promise;

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
var Mongoose = mongoose.model('Mongoose')

app.get('/', function(req, res) {
    Mongoose.find({}, function(err, mongooses){
        console.log("This should be the database:", mongooses)
        res.render('index', {"mongooses":mongooses});
    })
})
app.get('/new', function(req, res) {
    res.render('new');
})
app.get('/mongooses/:id', function(req, res) {
    Mongoose.find({_id:req.params.id}, function(err, mongoose){
        console.log(mongoose)
        res.render('profile', {"mongoose":mongoose});
    })
})
app.get('/mongooses/edit/:id', function(req, res) {
    Mongoose.find({_id:req.params.id}, function(err, mongoose){
        console.log(mongoose)
        res.render('edit', {"mongoose":mongoose});
    })
})
app.get('/mongooses/destroy/:id', function(req, res){
    Mongoose.remove({_id:req.params.id}, function(err){
        console.log("Successfully deleted this mongoose")
        res.redirect('/');
    })
})
app.post('/mongooses/:id', function(req, res){
    console.log("this works")
    Mongoose.findOne({_id:req.params.id}, function(err, mongoose){
        console.log(mongoose)
        console.log(err)
        mongoose.name = req.body.name
        mongoose.weight = req.body.weight
        mongoose.height = req.body.height
        mongoose.color = req.body.color
        mongoose.description = req.body.description
        mongoose.save(function(err){
            console.log("This is the mongoose: ", mongoose)
            res.redirect('/mongooses/'+mongoose._id);
        })
        
    })
})
app.post('/mongooses', function(req, res) {
    var mongoose = new Mongoose({name: req.body.name, height: req.body.height, weight:req.body.weight, color:req.body.color, description:req.body.description});
    mongoose.save(function(err){
        if(err){
            console.log('something went wrong');
        }
        else{
            console.log('successfully added quote');
        }
    })
    console.log("POST DATA", mongoose);
    res.redirect('/');
})
app.listen(8000, function() {
    console.log("listening on port 8000");
})
