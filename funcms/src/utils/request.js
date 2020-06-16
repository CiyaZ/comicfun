import Vue from 'vue';
import axios from 'axios';
import {rspStatusHandler} from '../consts';

let request = {
  get(url, {params = {}, headers = {}, success, failure}) {
    console.log('GET REQ', url, {params});
    axios({
      method: 'get',
      url, params, headers,
      responseType: 'json'
    }).then((resp) => {
      console.log('GET RESP', resp);
      if (success) {
        success(resp);
      }
    }).catch((err) => {
      console.error(err);
      let status = err.response.status;
      Vue.prototype.$message.error(rspStatusHandler('NET', status));
      if (status === 403) {
        Vue.prototype.$router.push('/login');
      } else {
        if (failure) {
          failure(err);
        }
      }
    });
  },
  post(url, {params = {}, headers = {}, data = {}, success, failure}) {
    console.log('POST REQ', url, {params, data});
    axios({
      method: 'post',
      url, params, headers, data,
      responseType: 'json'
    }).then((resp) => {
      console.log('POST RESP', resp);
      if (success) {
        success(resp);
      }
    }).catch((err) => {
      console.error(err);
      let status = err.response.status;
      Vue.prototype.$message.error(rspStatusHandler('NET', status));
      if (status === 403) {
        Vue.prototype.$router.push('/login');
      } else {
        if (failure) {
          failure(err);
        }
      }
    });
  },
  put(url, {params = {}, headers = {}, data = {}, success, failure}) {
    console.log('PUT REQ', url, {params, data});
    axios({
      method: 'put',
      url, params, headers, data,
      responseType: 'json'
    }).then((resp) => {
      console.log('PUT RESP', resp);
      if (success) {
        success(resp);
      }
    }).catch((err) => {
      console.error(err);
      let status = err.response.status;
      Vue.prototype.$message.error(rspStatusHandler('NET', status));
      if (status === 403) {
        Vue.prototype.$router.push('/login');
      } else {
        if (failure) {
          failure(err);
        }
      }
    });
  },
  delete(url, {params = {}, headers = {}, success, failure}) {
    console.log('DELETE REQ', url, {params});
    axios({
      method: 'delete',
      url, params, headers,
      responseType: 'json'
    }).then((resp) => {
      console.log('DELETE RESP', resp);
      if (success) {
        success(resp);
      }
    }).catch((err) => {
      console.error(err);
      let status = err.response.status;
      Vue.prototype.$message.error(rspStatusHandler('NET', status));
      if (status === 403) {
        Vue.prototype.$router.push('/login');
      } else {
        if (failure) {
          failure(err);
        }
      }
    });
  }
};

export default request;
