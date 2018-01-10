const express = require('express');
const app = express();

require('./server/config/middleware')(app);
require('./server/config/mongoose');
require('./server/config/routes')(app);


app.listen(8000, function() {
    console.log("listening on port 8000");
})
