
// turning the element with the ID dropbox into drop zone.
// let dropbox;
// https://developer.mozilla.org/en-US/docs/Web/API/File
// https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API
// https://html.spec.whatwg.org/multipage/dnd.html#dnd
// https://www.smashingmagazine.com/2018/01/drag-drop-file-uploader-vanilla-js/

// dropbox = document.getElementById("dropbox");
// // dropbox.addEventListener("dragenter", dragenter, false);
// // dropbox.addEventListener("dragover", dragover, false);
// // dropbox.addEventListener("drop", drop, false);
// dropbox.addEventListener()

// function dragenter(e) {
//     e.stopPropagation();
//     e.preventDefault();
//   }
  
//   function dragover(e) {
//     e.stopPropagation();
//     e.preventDefault();
//   }

//   function drop(e) {
//     e.stopPropagation();
//     e.preventDefault();
  
//     const dt = e.dataTransfer;
//     const file = dt.files;
  
//     handleFiles(file);
//   }

// function dropHandler(ev) {
//     console.log("File(s) dropped");
  
//     // Prevent default behavior (Prevent file from being opened)
//     ev.preventDefault();
  
//     if (ev.dataTransfer.items) {
//       // Use DataTransferItemList interface to access the file(s)
//       [...ev.dataTransfer.items].forEach((item, i) => {
//         // If dropped items aren't files, reject them
//         if (item.kind === "file") {
//           const file = item.getAsFile();
//           console.log(`… file[${i}].name = ${file.name}`);
//         }
//       });
//     } else {
//       // Use DataTransfer interface to access the file(s)
//       [...ev.dataTransfer.files].forEach((file, i) => {
//         console.log(`… file[${i}].name = ${file.name}`);
//       });
//     }
//   }

// function dragOverHandler(ev) {
//     console.log("File(s) in drop zone");
  
//     // Prevent default behavior (Prevent file from being opened)
//     ev.preventDefault();
// }

// const fileInput = document.getElementById('file');
// fileInput.onchange = () => {
//   const selectedFiles = [...fileInput.files];
//   console.log(selectedFiles);
// }

// function dragstartHandler(ev) {
//     // Add the target element's id to the data transfer object
//     ev.dataTransfer.setData("text/plain", ev.target.id);
//   }

//   window.addEventListener("DOMContentLoaded", () => {
//     // Get the element by id
//     const element = document.getElementById("upload_form");
//     // Add the ondragstart event listener
//     element.addEventListener("dragstart", dragstartHandler);
// });

// function dragstartHandler(ev) {
//     ev.dataTransfer.dropEffect = "copy";
// }

// function dragoverHandler(ev) {
//     ev.preventDefault();
//     ev.dataTransfer.dropEffect = "move";
//   }

// function dropHandler(ev) {
//     ev.preventDefault();
//     // Get the id of the target and add the moved element to the target's DOM
//     const data = ev.dataTransfer.getData("text/plain");
//     ev.target.appendChild(document.getElementById(data));
//   }
