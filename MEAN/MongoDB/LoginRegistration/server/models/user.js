 var mongoose = require('mongoose');

 var UserSchema = new mongoose.Schema({
     first_name: {
         type: String,
         required: [true, "Must enter first name"]
     },
     last_name: {
        type: String,
        required: [true, "Must enter last name"]
    },
     email: {
        type: String,
        required: [true, "Must enter a valid email address"]
    },
     password: {
        type: String,
        required: [true, "Must enter a password"],
        minlength: [8, "Password must be at least 8 characters long"],
    },
     dob: {
         type: Date
     },
 }, {timestamps: true})

 var User = mongoose.model('User', UserSchema);