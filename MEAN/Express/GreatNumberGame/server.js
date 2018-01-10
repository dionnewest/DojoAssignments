// require express
var express = require("express");
// path module -- try to figure out where and why we use this
var path = require("path");
var session = require('express-session');
// create the express app
var app = express();
var bodyParser = require('body-parser');
// use it!
app.use(session({secret: 'codingdojorocks'}));
app.use(bodyParser.urlencoded({ extended: true }));
// static content
app.use(express.static(path.join(__dirname, "./static")));
// setting up ejs and our views folder
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
// root route to render the index.ejs view
app.get('/', function(req, res) {
    if (req.session.temp != undefined){
        temp = temp
    }
    else{
        req.session.temp = Math.random() * 100
        req.session.temp = Math.floor(req.session.temp)
        temp = req.session.temp
        req.session.message = "Take a guess!"
    }
    if (req.session.body != undefined){
        var num = req.session.body.number
    }
    var message = req.session.message
    res.render("index", {num, message})
})
// post route for adding a user
app.post('/number', function(req, res) {
    req.session.body = req.body
    if(req.body.number > req.session.temp){
        req.session.message = "Your guess: "+ req.body.number +", is too high. Try again"
    }
    if(req.body.number < req.session.temp){
        req.session.message = "Your guess: "+ req.body.number +", is too low. Try again"
    }
    if(req.body.number == req.session.temp){
        req.session.message = "Your guess: "+ req.body.number +", is correct! Hit reset to play again :)"
    }
    res.redirect("/")
})
app.post('/reset', function(req, res) {
    req.session.body = undefined
    req.session.temp = undefined
    res.redirect("/")
})
// tell the express app to listen on port 8000
app.listen(8000, function() {
 console.log("listening on port 8000");
});
