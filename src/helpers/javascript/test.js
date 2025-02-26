import { sample } from 'lodash';

export const generateFlower = () => {
  const chars = ['•', '·'];
  const size = Math.floor(Math.random() * 20) + 4;
  const offset = sample(['top-[10px]', 'top-[-10px]', 'top-[-5px]', 'top-[5px]', '']);

  [...Array(size)].forEach((_, i) => {
    // <p class={`relative ${offset}`}>{_.sample(chars)}</p>
    console.log(i);
    console.log(offset)
  });
}

console.log('kikouuuuu')
generateFlower()