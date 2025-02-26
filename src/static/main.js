// import './style.css'
import javascriptLogo from './javascript.svg'
import viteLogo from '/vite.svg'
import { setupCounter } from './js/counter.js'

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

// document.querySelector('#app').innerHTML = `
//   <div>
//     <a href="https://vite.dev" target="_blank">
//       <img src="${viteLogo}" class="logo" alt="Vite logo" />
//     </a>
//     <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
//       <img src="${javascriptLogo}" class="logo vanilla" alt="JavaScript logo" />
//     </a>
//     <h1>Hello Vite!</h1>
//     <div class="card">
//       <button id="counter" type="button"></button>
//     </div>
//     <p class="read-the-docs">
//       Click on the Vite logo to learn more
//     </p>
//   </div>
// `

// setupCounter(document.querySelector('#counter'))


