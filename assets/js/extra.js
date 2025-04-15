import SimpleParallax from 'https://cdn.jsdelivr.net/npm/simple-parallax-js@6.1.1/vanilla/+esm'

document$.subscribe(() => {
    const image = document.querySelector('.bg-hero');

    if (image) {
        new SimpleParallax(image, {
            orientation: "up",
        })
    }
})

