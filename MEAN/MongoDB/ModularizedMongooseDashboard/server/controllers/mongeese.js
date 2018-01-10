var mongoose = require('mongoose');
var Mongoose = mongoose.model('Mongoose');
module.exports = {
  show: function(req, res) {
    Mongoose.find({}, function(err, mongeese) {
      res.render('index', {mongeese:mongeese});
    })
  },
  create: function(req, res) {
    var mongoose = new Mongoose({name: req.body.name, height: req.body.height, weight:req.body.weight, color:req.body.color, description:req.body.description});
    mongoose.save(function(err){
      if(err){
          console.log('something went wrong');
      }
      else{
          console.log('successfully added quote');
      }
      res.redirect('/')
    })
  },
  new: function(req, res){
    res.render('new');
  },
  update: function(req, res){
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
          res.redirect('/mongeese/'+mongoose._id);
      })
    })
  },
  destroy: function(req, res){
    Mongoose.remove({_id:req.params.id}, function(err){
      console.log("Successfully deleted this mongoose")
      res.redirect('/');
    })
  },
  profile: function(req, res){
    Mongoose.find({_id:req.params.id}, function(err, mongoose){
      console.log(mongoose)
      res.render('profile', {"mongoose":mongoose});
    })
  },
  edit: function(req, res){
    Mongoose.find({_id:req.params.id}, function(err, mongoose){
      console.log(mongoose)
      res.render('edit', {"mongoose":mongoose});
    })
  }
}
