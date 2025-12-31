import MiniCssExtractPlugin from "mini-css-extract-plugin"
import { ModuleOptions } from "webpack"
export function buildLoaders():ModuleOptions['rules'] {
    return [
        {
            test:/\.module.s[ac]ss$/i,
            use: [
                MiniCssExtractPlugin.loader,
                    {
                    loader: 'css-loader',
                    options: {
                        modules: {
                            localIdentName: '[name]__[local]--[hash:base64:5]',
                            exportLocalsConvention: 'camelCase',
                            namedExport: false,
                        },
                        esModule: true
                    }
                    },
                'sass-loader'
            ],
        },
        {
            test:/\.css$/i,
            use:[MiniCssExtractPlugin.loader, 'css-loader']
        },
        {
            test: /\.tsx?$/,
            use: 'ts-loader',
            exclude: /node_modules/,
        },
        {
            test: /\.(png|jpg|jpeg\gif)$/i,
            type: 'asset/resource',
        },
        {
            test: /\.svg$/,
            use: ['@svgr/webpack'],
        }
    ]
}