import { defineStore } from 'pinia'

export const useGlobalStore = defineStore('global', {
  state: () => {
    let initial_state = { authtoken: null, userinfo: null };
    let part = document.cookie
                      .split('; ')
                      .filter((p) => p.startsWith('authtoken='));

    if (part.length === 0) return initial_state

    let token = part[0].split('=')[1];

    if (token.trim().length === 0) return initial_state

    initial_state.authtoken = token

    fetch('http://127.0.0.1:8000/api/userinfo', {
      headers: {
        Authorization: `Token ${initial_state.authtoken}`,
      }
    }).then((res) => res.json())
      .then((data) => {
        initial_state.userinfo = data;
      })

    return initial_state
  },

  getters: {
    is_authenticated: (state) => state.authtoken !== null,
  },

  actions: {
    async login(username, password) {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/auth/login', {
          method: 'POST',
          mode: 'cors',
          body: new URLSearchParams({ username, password }),
        });

        if (response.status === 200) {
          const data = await response.json();
          this.authtoken = data['token'];

          document.cookie = `authtoken=${this.authtoken}`;

          const userinfo = await fetch('http://127.0.0.1:8000/api/userinfo', {
            headers: {
              Authorization: `Token ${this.authtoken}`,
            }
          });

          this.userinfo = await userinfo.json();

          return true;
        } else {
          return false;
        }
      } catch (err) {
        throw err;
      }
    },

    logout() {
      this.authtoken = null;
      this.userinfo = null;
      document.cookie = 'authtoken=';
    },

    async request_api_endpoint(
      endpoint,
      method = 'get',
      payload = null,
      additional_headers = {},
    ) {
      if (!this.is_authenticated) {
        throw new Error("Authentication required");
      }

      try {
        const url = `http://127.0.0.1:8000/${endpoint}`;
        
        // Only add the Authorization header if authtoken is non-empty.
        let headers = additional_headers;
        headers["Authorization"] = `Token ${this.authtoken}`;
        
        const options = {
          method: method,
          mode: 'cors',
          headers: headers,
        };

        if (payload && method.toLowerCase() === 'get') {
          options.body = new URLSearchParams(payload);
        } else if (payload) {
          options.body = payload;
        }

        const response = await fetch(url, options);
        
        // Optionally check for errors before returning the JSON.
        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(JSON.stringify(errorData));
        }
        
        return await response.json();
      } catch (err) {
        throw err;
      }
    },

    async download_file(endpoint) {
      try {
        if (!this.is_authenticated) {
          throw new Error("Authentication required");
        }

        const url = `http://127.0.0.1:8000/${endpoint}`;
        let options = {
          method: 'get',
          mode: 'cors',
          headers: {
            Authorization: `Token ${this.authtoken}`
          }
        };

        let response = await fetch(url, options);
        if (!response.ok)
          throw new Error(await response.text());

        let data = await response.blob();

        let filename = response.headers.get('Content-Disposition');
        filename = filename.split(';')[1];
        filename = filename.split('=')[1].replaceAll('\"', '');

        let dummy_element = document.createElement('a');
        dummy_element.href = window.URL.createObjectURL(data);
        dummy_element.download = filename;
        document.body.appendChild(dummy_element);
        dummy_element.click();
        dummy_element.remove();

      } catch(err) {
        throw err;
      }
    }
  },
})

