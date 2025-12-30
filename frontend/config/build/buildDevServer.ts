import { Configuration } from "webpack-dev-server"

type Params = {
    isDev: boolean,
    PORT: number
}

export function buildDevServer(params: Params):Configuration {
    return params.isDev ? {
            port: params.PORT || 5000,
            open: true
        } : undefined
}