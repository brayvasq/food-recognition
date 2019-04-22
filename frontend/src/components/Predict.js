import React, {Component} from 'react';
import './Predict.css';
import axios from 'axios';
import ReactJson from 'react-json-view';
import FileBase64 from 'react-file-base64';

class Predict extends Component{

    constructor(props){
        super(props)
        this.state = {
            url_get_param: '',
            url_post_param: '',
            respuesta: []
        }
        this.getPetition = this.getPetition.bind(this);
        this.postPetition = this.postPetition.bind(this);
        this.handleChangeGet = this.handleChangeGet.bind(this);
        this.handleChangePost = this.handleChangePost.bind(this);
    }

    handleChangeGet(event) {
        this.setState({url_get_param: event.target.value});
    }

    handleChangePost(event) {
        this.setState({url_post_param: event.target.value});
    }

    async getPetition(){
        const resp = await axios.get(`http://localhost:5000/predecir?idPrueba=${this.state.url_get_param}`);
        this.setState({respuesta: resp.data});
        console.log(resp.data)
        console.log(this.state.respuesta)
    }

    async postPetition(){
        let bodyFormData = new FormData();
        //console.log(this.state.url_post_param);
        
        bodyFormData.set('imagen', this.state.url_post_param);
        const resp = await axios({
            method: 'post',
            url: 'http://localhost:5000/predecir',
            data: bodyFormData,
            config: { headers: {'Content-Type': 'multipart/form-data' }}
            })
        this.setState({respuesta: resp.data});
        console.log(resp.data)
        //console.log(this.state.respuesta)
    }

    getFiles(files){
        //this.setState({ files: files })
        console.log(files)
        let value = files.base64.replace('data:image/jpeg;base64,','');
        this.setState({url_post_param: value});
    }

    render(){
        return (
            <div className="center">
                <div className="box">
                    <div className="columns">
                        <div class="column separator">
                            <h1 className="title is-1"> Interpreter </h1>
                            <form>
                                <div className="field">
                                    <label className="label">Id Image</label>
                                    <div className="control">
                                        <input className="input" type="text" placeholder="Username" value={this.state.url_get_param} onChange={this.handleChangeGet}/>
                                    </div>
                                </div>
                                <div className="field">
                                    <label className="label">Image Base64</label>
                                    <div className="control">
                                        {/*<input className="input" type="password" placeholder="Password" />*/}
                                        <textarea class="textarea" placeholder="10 lines of textarea" rows="10" value={this.state.url_post_param} onChange={this.handleChangePost}></textarea>
                                        <div class="file">
                                            <label class="file-label">
                                                <div className="file-hidden">
                                                    <FileBase64
                                                    multiple={ false }
                                                    onDone={this.getFiles.bind(this)  } />
                                                </div>
                                                
                                                <span class="file-cta">
                                                <span class="file-icon">
                                                    <i class="fas fa-upload"></i>
                                                </span>
                                                <span class="file-label">
                                                    Choose a file…
                                                </span>
                                                </span>
                                            </label>
                                        </div>
                                    
                                    </div>
                                </div>

                                <div className="buttons">
                                    <span className="button is-success" onClick={this.getPetition}>GET</span>
                                    <span className="button is-info" onClick={this.postPetition}>POST</span>
                                </div>
                            </form>
                        </div>
                        <div className="column">
                        <form>
                                <div className="field">
                                    <label className="label">Image Base64</label>
                                    <div className="control">
                                        <ReactJson src={this.state.respuesta}></ReactJson>
                                    </div>
                                </div>

                            </form>
                        
                        </div>
                    </div>
                            
                </div>
            </div>
        )
    }
}

export default Predict;
