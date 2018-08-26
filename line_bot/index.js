var exec = require('child_process').exec;
var filename = 'main.py'
let linebot = require('linebot'),
    express = require('express');
const config = require('./package.json'),
    util = require('util');
let bot = linebot({
    channelId: '1535824257',
    channelSecret: '1f9fff19d613da0a7ebeab77703cdcaa',
    channelAccessToken: 'rqi6Ooc9nTf11tUk0ZsGl570J+0skjOCQ1vLBGy1HcR5J1I951ZxclBfYTxgM1J8Uien3Te7Dn0M5qA9egq+m5f4PnQoixMnwqRmoO2COG3hu9gUFzLhPBawoPitQvFQXCXJva4OVq5WUYi/kYWCuAdB04t89/1O/w1cDnyilFU='
});
var text = ""
const linebotParser = bot.parser(),
    app = express();

bot.on('message', function(event) {
    // 把收到訊息的 event 印出來
    if (event.message.type = 'text') {
        var msg = event.message.text;
        exec('python' + ' ' + filename + ' ' + msg, function (err, stdout, stderr) {
            if (err) {
                console.log('stderr', err);
            }
            if (stdout) {
                console.log('stdout', stdout);
                event.reply(stdout).then(function(data) {
                // success
                    console.log(stdout);
                }).catch(function(error) {
                // error
                    console.log('error');
                });
            }
        });
    }
});


app.post('/callback', linebotParser);
// 在 localhost 走 8080 port
let server = app.listen(process.env.PORT || 8080, function() {
    let port = server.address().port;
    console.log("My Line bot App running on port", port);
});