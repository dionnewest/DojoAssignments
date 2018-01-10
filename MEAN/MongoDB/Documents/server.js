var express = require('express');

var app = express();

var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended:true}));

var path = require('path');

var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/basic_mongoose');
mongoose.Promise = global.Promise;

var UserSchema = new mongoose.Schema({
    name: {type: String, required: true, min: [3, 'Name must be at least 3 characters long']},
    age: {type: Number, required: true, min: [1, 'Must enter an age.']}
}, {timestamps: true});

mongoose.model('User', UserSchema);
var User = mongoose.model('User')

app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

app.get('/', function(req, res){
    User.find({}, function(err, users) { 
        if(users.length < 1){
            console.log("No users found")
        }
        else{
            console.log(users)
        }
        res.render('index', {"users":users});
    })
})

app.post('/users', function(req, res) {
    console.log("POST DATA", req.body);
    var user = new User({name: req.body.name, age: req.body.age});
    user.save(function(err) {
      if(err) {
        console.log('something went wrong');
      } else {
        console.log('successfully added a user!');
        res.redirect('/');
      }
    })
  })

app.listen(8000, function(){
})