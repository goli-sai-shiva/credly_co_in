document.addEventListener('DOMContentLoaded', function() {
    const posts = document.querySelectorAll('.post');
    
    posts.forEach(post => {
        post.addEventListener('click', function() {
            this.style.backgroundColor = '#f0f0f0';
        });
    });
});