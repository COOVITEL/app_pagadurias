module.exports = {
    content: [
        "./src/**/*.{html,js,ts,jsx,tsx}",
        "../templates/**/*.html",
      ],
    theme: {
        extend: {
            colors: {
                blue:{
                    '450': '#262d63',
                    '550': '#363f84',
                    '650': '#38407a',
                    '750': '#444e99',
                }
            }
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
