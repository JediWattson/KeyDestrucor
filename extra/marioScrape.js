'use-strict'
const $ = require('cheerio');
const rp = require('request-promise');
const fs = require('fs')
const request = require('request');

function download(uri, filename, callback){
  return request.head(uri, function(err, res, body){
    return request(uri,{
      headers: {
        'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
      }
    }).pipe(fs.createWriteStream(filename)).on('close', callback);
  });
};


function init(){

  rp(`https://nesmaps.com/maps/SuperMarioBrothers/SuperMarioBrothersBG.html`)
  .then(function(html){
    if(!Boolean(html)){
      console.log("DONE")
      return null
    }

    const img = $('img', html)
    img.each(function(i, elem){

      download(
        `https://nesmaps.com/maps/SuperMarioBrothers/${this.attribs.src}`,
        `../mariobg/noMario${i}.png`,
        function(){
          console.log(`downloaded ${i}`);
          //init(next, num+1)
        }
      )
    })

  })
  .catch(function(err){
    //handle error
  });
}
init()
