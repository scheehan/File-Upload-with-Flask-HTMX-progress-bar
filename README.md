[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://camo.githubusercontent.com/44da37f0f02bf104f0650fa5f2c754ed3f6166066c9210f31bacb9e63d60736e/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f70796261646765732e737667)

# File Upload web app with Flask and HTMX progress bar

- In this example, file upload with submit button via ajax, along with a progress bar. This implementation with JavaScript using some utility methods in htmx.
--- 
- Here is the steps to implement htmx into a typical file upload web app

1. install htmx library
- In order to have htmx support for your website, we need to install htmx library on to your web server, so that allows you to access modern browser features directly from HTML.
donwload htmx.min.js via [unpkg.com](https://unpkg.com/htmx.org@1.9.8/dist/htmx.min.js). Htmx is a dependency-free, browser-oriented javascript library. This means that using it is as simple as adding a <script> tag to your document head. No need for complicated build steps or systems.

code snipit:  
`<script src="/static/js/htmx.min.js"></script>`

- CDN is another way to install htmx library. refer to link for more info.  
https://htmx.org/docs/#via-a-cdn-e-g-unpkg-com

2. Add htmx tag into html form tag as attribute. all htmx comes with hx prefix. 
'''
`<form id="my-form"  
            hx-encoding="multipart/form-data"
            hx-post="/uploads"
            hx-target="#list_results"
            hx-on::after-request="if(event.detail.successful) this.reset()"
        >`
'''  



[![Watch the video](https://github.com/scheehan/File-Upload-with-Flask-HTMX-progress-bar/blob/master/images/Track%20Your%20File%20Uploads.png)](https://youtu.be/IpMRus-FLPk)
