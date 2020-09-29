import React from "react";
import "./App.css";
import Tasks from "./Tasks";
export default class App extends React.Component {
  constructor() {
    super();
    this.state = {
      taskList: [],
      activeTask: {
        author: null,
        id: null,
        title: "",
        complete: false,
      },
      editing: false,
      currentAuth: window.author,
    };
    this.fetchTasks = this.fetchTasks.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.getCookie = this.getCookie.bind(this);
    this.beginEdit = this.beginEdit.bind(this);
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
  fetchTasks() {
    fetch("http://127.0.0.1:8000/api/task-list/" + this.state.currentAuth + "/")
      .then((response) => response.json())
      .then((jsonData) =>
        this.setState({
          taskList: jsonData,
        })
      );
  }
  componentDidMount() {
    this.fetchTasks();
  }
  handleSubmit(e) {
    e.preventDefault();
    var url = "http://127.0.0.1:8000/api/task-create/";
    if (this.state.editing == true) {
      url =
        "http://127.0.0.1:8000/api/task-update/" +
        this.state.activeTask.id +
        "/";
      this.setState({
        editing: false,
      });
    }
    var csrftoken = this.getCookie("csrftoken");
    fetch(url, {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify(this.state.activeTask),
    })
      .then((response) => {
        // console.log(response);
        this.fetchTasks();
        this.setState({
          activeTask: {
            id: null,
            title: "",
            complete: false,
          },
        });
      })
      .catch((error) => {
        // console.log("Error is: ", error);
      });
  }
  handleChange(e) {
    const newTitle = e.target.value;
    this.setState({
      activeTask: {
        ...this.state.activeTask,
        author: window.author,
        title: newTitle,
      },
    });
  }
  beginEdit(task) {
    this.setState({
      activeTask: {
        author: window.author,
        id: task.id,
        title: task.title,
        complete: task.complete,
      },
      editing: true,
    });
  }
  render() {
    const tasksMapped = this.state.taskList.map((index) => (
      <Tasks
        data={index}
        fetchTasks={this.fetchTasks}
        beginEdit={this.beginEdit}
      />
    ));
    return (
      <div className="MainWrapper shadow-lg">
        <div className="FormDiv">
          <form className="form-group Form" onSubmit={this.handleSubmit}>
            <input
              type="text"
              maxLength="32"
              placeholder="Create a Task"
              value={this.state.activeTask.title}
              className="form-control"
              name="inputTitle"
              onChange={this.handleChange}
            />
            <input
              type="Submit"
              className="SubmitTask btn"
              name="Create"
              value="Conjure"
            />
          </form>
        </div>
        <div className="countWrapper">
          {this.state.activeTask.title.length} / 32
        </div>
        <div className="TasksWrapper">{tasksMapped}</div>
      </div>
    );
  }
}
