'use strict'

async function getPhrase(event) {
    const url = "/api/getphrase/"
    let resp = await fetch(url)
    let json = await resp.json()
    let phrase = json["phrase"]
    let newP = document.createElement("p")
    let pText = document.createTextNode(phrase)
    newP.appendChild(pText)
    let div = document.getElementById("phrases")
    div.appendChild(newP)
}

let a = document.getElementById("get-phrase")
a.addEventListener("click", getPhrase)
