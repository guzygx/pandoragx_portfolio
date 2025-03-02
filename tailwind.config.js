module.exports = {
  content: [
    './app/index.html',
    './app/**/*.html',
    './app/**/*.{js,ts,jsx,tsx}'
  ],
  theme: {
    extend: {
      colors: {
        brand: '#4F46E5',
      },
      spacing: {
        '128': '32rem',
      }
    },
  },
  plugins: [],
}