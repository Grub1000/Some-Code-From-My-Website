import React from "react";
import App from "./App";

export default class Tasks extends React.Component {
  constructor() {
    super();
    this.state = {};
    this.TaskDelete = this.TaskDelete.bind(this);
    this.getCookie = this.getCookie.bind(this);
  }
  getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  TaskDelete(id) {
    let url = "http://127.0.0.1:8000/api/task-delete/" + id + "/";
    console.log(id);
    var csrftoken = this.getCookie("csrftoken");
    fetch(url, {
      method: "DELETE",
      headers: {
        "content-type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    }).then((response) => {
      this.props.fetchTasks();
    });
  }
  render() {
    const self = this;
    return (
      <div className="Task ">
        <div className="TaskTitle font-weight-light">
          {this.props.data.title}
        </div>
        <button
          className="UpdateTask btn"
          onClick={() => self.props.beginEdit(self.props.data)}
        >
          Edit
        </button>
        <button
          className="DeleteTask btn"
          onClick={() => self.TaskDelete(self.props.data.id)}
        >
          <i class="fas fa-minus-square fa-2x"></i>
        </button>
      </div>
    );
  }
}
