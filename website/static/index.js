function deleteNote(noteId) {
  fetch('/delete-note', {
    method: 'POST',
    body: JSON.stringify({ noteId: noteId})
  })
  .then((_res) => {
    window.location.href = "/notes"
  })
}

// theme change

const lightDarkBtn = document.getElementById('theme')
const body = document.body

const theme = localStorage.getItem('theme')

if (theme) {
  body.classList.add(theme)
}


lightDarkBtn.onclick = () => {
  if (body.classList.contains('light')) {
    body.classList.remove('light')
    body.classList.add('dark')
    localStorage.setItem('theme', 'dark')
  } else {
    body.classList.remove('dark')
    body.classList.add('light')
    localStorage.setItem('theme', 'light')
  }
}