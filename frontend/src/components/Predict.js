import React, {Component} from 'react';
import './Predict.css';
import axios from 'axios';
import ReactJson from 'react-json-view';
import FileBase64 from 'react-file-base64';

/**
 * Componente que funciona como el formulario de creación de gastos
 */
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
        this.handleChangePost = this.handleChangePost.bind(this)
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
            <div>
                {/** GET Petition */}
                <div>
                    <h1>GET prediction</h1>
                    <h2>Url to request: http://localhost:5000/predecir?idPrueba={this.state.url_get_param}</h2>
                    <div className="field is-horizontal">
                        <div className="field-label is-normal">
                            <label className="label">Id Prueba</label>
                        </div>
                        <div className="field-body">
                            <div className="field">
                            <p className="control">
                                <input className="input" type="text" placeholder="Id Prueba" value={this.state.url_get_param} onChange={this.handleChangeGet}/>
                            </p>
                            </div>
                        </div>
                    </div>
                    <a className="button is-success" onClick={this.getPetition}>Success</a>
                    <textarea class="textarea" placeholder="10 lines of textarea" rows="10" value={JSON.stringify(this.state.respuesta)}></textarea>
                    { /** <ReactJson src={this.state.respuesta} /> */}
                </div>
                {/** End GET Petition */}
                {/** POST Petition */}
                <div>
                    <h1>POST prediction</h1>
                    <h2>Url to request: http://localhost:5000/predecir</h2>
                    
                    <textarea class="textarea" placeholder="10 lines of textarea" rows="10" value={this.state.url_post_param} onChange={this.handleChangePost}></textarea>
                    <FileBase64
                        multiple={ false }
                        onDone={ this.getFiles.bind(this) } />
                    <a className="button is-success" onClick={this.postPetition}>Success</a>
                </div>
                {/** End Post Petition */}
            </div>
        )
    }
}

export default Predict;
