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