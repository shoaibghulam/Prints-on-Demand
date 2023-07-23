/** @type {import('tailwindcss').Config} */
module.exports = {
 
  content: 
  [
    "./templates/**/*.{html,js}",
   
],
  theme: {
    extend: {
      colors:{
        'primary':"#ff6759"
      }
    },
  },
  plugins: [
    require('flowbite/plugin')

  ],
  prefix: 'tw-',
}