const titleInput = document.querySelector('input[name=tittle]');
const slugInput = document.querySelector('input[name=slug]');

const slug = (val)=>{
return val.toString().toLowerCase().trim()
    .replace(/&/g/,'-and-')
    .replace(/[\s\W-]+/g,'-')
};
titleInput.addEventListener('key',(e)=>{
    slugInput.setAttribute('value',slug(titleInput.value))
});
