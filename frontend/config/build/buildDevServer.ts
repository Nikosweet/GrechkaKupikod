import { Configuration } from "webpack-dev-server"

type Params = {
    PORT: number
}

export function buildDevServer(params: Params):Configuration {
    return {
            port: params.PORT || 5000,
            open: true,
            historyApiFallback: true,
            hot: true
        }
}