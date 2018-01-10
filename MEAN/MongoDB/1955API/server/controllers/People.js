 var mongoose = require('mongoose');
var People = mongoose.model('People');
module.exports = {
    show: function(req, res){
        People.find({}, function(err, people){
            res.json({people:people});
        })
    },
    create: function(req, res){
        var person = new People({name: req.params.name})
        person.save(function(err){
            res.redirect('/')
        })
    },
    remove: function(req, res){
        People.remove({name: req.params.name}, function(err){
            res.redirect('/')
        })
    },
    profile: function(req, res){
        People.find({name: req.params.name}, function(err, person){
            console.log(person)
            res.json({person:person});
        })
    }
}