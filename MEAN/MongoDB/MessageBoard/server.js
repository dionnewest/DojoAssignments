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

var CommentSchema = new mongoose.Schema({
    name:{
        type: String,
        required: true,
        minlength: [4, "Name must be at least 4 characters"]
    },
    comment:{
        type: String,
        required: true,
        minlength: [10, "Comment must be at least 10 characters"]
    }
})

var MessageSchema = new mongoose.Schema({
    name:{
        type: String,
        required: true,
        minlength: [4, "Name must be at least 4 characters"]
    },
    message:{
        type: String,
        required: true,
        minlength: [10, "Message must be at least 10 characters"]
    },
    comments: [CommentSchema]
})

mongoose.model('Message', MessageSchema);
var Message = mongoose.model('Message')

mongoose.model('Comment', CommentSchema);
var Comment = mongoose.model('Comment')

app.get('/', function(req, res) {
    Message.find({}, function(err, messages){
        console.log(messages)
        res.render('index', {'messages':messages});
    })
})
app.post('/post_message', function(req, res) {
    var message = new Message({name: req.body.name, message: req.body.message});
    message.save(function(err){
        if(err){
            console.log('something went wrong');
        }
        else{
            console.log('successfully added message');
        }
        res.redirect('/');
    })
    console.log("POST DATA", message)
})
app.post('/post_comment/:id', function(req, res) {
    var comment = new Comment({name: req.body.name, comment: req.body.comment});
    Message.findOne({_id:req.params.id}, function(err, message){
        message.comments.push(comment)
        message.save(function(err){
            if(err){
                console.log('something went wrong');
            }
            else{
                console.log('successfully added message');
            }
            res.redirect('/');
        })
    })
})
app.listen(8000, function() {
    console.log("listening on port 8000");
})
