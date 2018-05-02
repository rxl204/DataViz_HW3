class ZipcodeForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      ZipCode: '11201',
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  handleSubmit(event) {
   var spec = `/vis/${this.state.ZipCode}`;
    vegaEmbed('#vis', spec, {actions:false});
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Zip Code &nbsp;
          <input
            type="text"
            name="ZipCode"
            value={this.state.ZipCode}
            onChange={this.handleChange} />
        </label>
        <input type="submit" value="Update" />
      </form>
    );
  }
}

ReactDOM.render(
  <div>
    <ZipcodeForm/>
  </div>,
  document.getElementById('ui')
);
