
document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');
  const myList = document.querySelector('.my_list');

  addItem.addEventListener('click', () => {
    const liElement = document.createElement('li');
    liElement.textContent = 'Item';
    myList.append(liElement);
  });

  removeItem.addEventListener('click', () => {
    const liRemove = document.querySelector('.my_list li:last-child');
    liRemove.remove();
  });

  clearList.addEventListener('click', () => {
    const allLiElements = document.querySelectorAll('.my_list li');
    allLiElements.forEach(li => li.remove());
  });
});
