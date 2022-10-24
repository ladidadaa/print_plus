let current = undefined

// function changeTab(){
//     for (let i = 0; i < tabs.length; ++i){
//         const tab = tabs[i]
//         if (current.classList[1] == tab.classList[1]){
//             return tab
//         }
//     }
// }
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

// const items = document.getElementsByClassName('nav__element')
// for (let i = 0; i < items.length; ++i) {
//   const item = items[i]
//   item.addEventListener('mouseover', onMouseover)
// }
// tabs = [document.getElementsByClassName('documents')[1], document.getElementsByClassName('photo')[1], 
//         document.getElementsByClassName('document_photo')[1], document.getElementsByClassName('vizitki')[1], 
//         document.getElementsByClassName('polk')[1]]

elements = [document.getElementsByClassName('documents')[0], document.getElementsByClassName('photo')[0], 
            document.getElementsByClassName('document_photo')[0], document.getElementsByClassName('vizitki')[0], 
            document.getElementsByClassName('polk')[0]]
for (let i = 0; i < elements.length; ++i) {
    const element = elements[i]
    element.addEventListener('mouseover', onMouseover)
}