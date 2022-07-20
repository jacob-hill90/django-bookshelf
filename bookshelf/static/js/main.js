console.log("JS working?")

function saveBook(){
  title = document.getElementById("newTitle").value
  author = document.getElementById("newAuthor").value
  description = document.getElementById("newDescription").value

  axios.post("", {title : title, author : author, description: description}).then((response) => {
    window.location.href = "../../"
	})

}

function editBook(){
  title = document.getElementById("newTitle").value
  author = document.getElementById("newAuthor").value
  description = document.getElementById("newDescription").value

  axios.post("", {title : title, author : author, description: description}).then((response) => {
    window.location.href = "../../../"
	})

}

