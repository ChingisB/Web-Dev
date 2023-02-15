let style = new Array("Jazz", "Blues");
style.push("Rock-n-Roll");
style[Math.floor(style.length / 2)] = "Classics";
alert(style.shift())
style.unshift('Reggae')
style.unshift("Rap")