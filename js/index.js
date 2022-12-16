let current = undefined

function changeTab(current){
    return tab = document.getElementsByClassName(current.classList[1])[1]
}

function onMouseover() {
    if (current) {
        changeTab(current).hidden = true
    }
    current = this
    changeTab(current).hidden = false
}

elements = [document.getElementsByClassName('documents')[0], document.getElementsByClassName('photo')[0], 
            document.getElementsByClassName('document_photo')[0], document.getElementsByClassName('vizitki')[0], 
            document.getElementsByClassName('polk')[0]]
for (let i = 0; i < elements.length; ++i) {
    const element = elements[i]
    element.addEventListener('mouseover', onMouseover)
}

//Загрузка файлов

var input = document.querySelector('.file');
var preview = document.querySelector('.file_preview');

input.style.opacity = 0;

input.addEventListener('change', updateImageDisplay);

function updateImageDisplay() {
    while(preview.firstChild) {
      preview.removeChild(preview.firstChild);
    }
  
    var curFiles = input.files;
    if(curFiles.length === 0) {
      var para = document.createElement('p');
      para.textContent = 'Ни один файл для загрузки не выбран';
      preview.appendChild(para);
    } else {
      var list = document.createElement('ol');
      preview.appendChild(list);
      for(var i = 0; i < curFiles.length; i++) {
        var listItem = document.createElement('li');
        var para = document.createElement('p');
        if(validFileType(curFiles[i])) {
          para.textContent = curFiles[i].name + ', ' + returnFileSize(curFiles[i].size) + '.';
          var image = document.createElement('img');
          image.src = window.URL.createObjectURL(curFiles[i]);
  
          listItem.appendChild(image);
          listItem.appendChild(para);
  
        } else {
          para.textContent = curFiles[i].name + ' : Не подходящий файл, попробуйте еще раз';
          listItem.appendChild(para);
        }
  
        list.appendChild(listItem);
      }
    }
  }

  var fileTypes = [
    'image/jpeg',
    'image/pjpeg',
    'image/png',
    'application/msword',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/pdf'
  ]
  
  function validFileType(file) {
    for(var i = 0; i < fileTypes.length; i++) {
      if(file.type === fileTypes[i]) {
        return true;
      }
    }
  
    return false;
  }

  function returnFileSize(number) {
    if(number < 1024) {
      return number + 'bytes';
    } else if(number > 1024 && number < 1048576) {
      return (number/1024).toFixed(1) + 'KB';
    } else if(number > 1048576) {
      return (number/1048576).toFixed(1) + 'MB';
    }
  }