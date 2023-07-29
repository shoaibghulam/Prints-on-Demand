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
      },
      fontSize:{
      
        'f35':"35px",
        'f14':"14px",
        'f16':"16px",
        'f18':"18px",
      },
      fontFamily: {
        'roboto': ['Roboto', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('flowbite/plugin')

  ],
  prefix: 'tw-',
}