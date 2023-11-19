[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://camo.githubusercontent.com/44da37f0f02bf104f0650fa5f2c754ed3f6166066c9210f31bacb9e63d60736e/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f70796261646765732e737667)

# File Upload web app with Flask and HTMX progress bar

- In this example, file upload with submit button via ajax, along with a progress bar. This implementation with JavaScript using some utility methods in htmx.
--- 
- Here is the steps to implement htmx into a typical file upload web app

1. install htmx library
- In order to have htmx support for your website, we need to install htmx library on to your web server, so that allows you to access modern browser features directly from HTML.
donwload htmx.min.js via [unpkg.com](https://unpkg.com/htmx.org@1.9.8/dist/htmx.min.js). Htmx is a dependency-free, browser-oriented javascript library. This means that using it is as simple as adding a <script> tag to your document head. No need for complicated build steps or systems.

Code snippet:  
~~~
            <script src="/static/js/htmx.min.js"></script>
~~~

- CDN is another way to install htmx library. refer to link for more info.  
https://htmx.org/docs/#via-a-cdn-e-g-unpkg-com

2. Add htmx tag into html form tag as attribute. all htmx comes with hx prefix.  
Code snippet:  
~~~
            <form id="my-form"  
                        hx-encoding="multipart/form-data"
                        hx-post="/uploads"
                        hx-target="#list_results"
                        hx-on::after-request="if(event.detail.successful) this.reset()"
            >
~~~  
- We have a form of type multipart/form-data so that the file will be properly encoded with hx-enconding attribute, replacing normal html enctype attibute. 
- We post the form to /uploads with hx-post, send form data to target URL.
- we forward the response output to target div id "#list_results" with hx-target attibute.
- we ensure a form reset only after a successful event with if(event.detail.successful) this.reset()
- We have a progress element to show the file upload progress with id my-progress.

~~~
            <progress id="my-progress" value="0" max="100"></progress>
~~~

- We listen for the htmx:xhr:progress event refer back to id my-progress and update the value attribute of the progress bar based on the loaded and total properties in the event detail.  
JavaScript Code snippet:  
~~~
            <script>
                htmx.on('#my-form', 'htmx:xhr:progress', function(evt) {
                  htmx.find('#my-progress').setAttribute('value', evt.detail.loaded/evt.detail.total * 100)
                });
            </script>
~~~

[![Watch the video](https://github.com/scheehan/File-Upload-with-Flask-HTMX-progress-bar/blob/master/images/Track%20Your%20File%20Uploads.png)](https://youtu.be/IpMRus-FLPk)
