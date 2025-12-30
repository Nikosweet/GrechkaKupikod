import { Configuration } from 'webpack'

import HtmlWebpackPlugin from'html-webpack-plugin'
import MiniCssExtractPlugin from 'mini-css-extract-plugin'

export function buildPlugins(html: string):Configuration['plugins'] {
    return [
            new HtmlWebpackPlugin({template: html}),
            new MiniCssExtractPlugin({
                filename: 'css/[name].[contenthash:8].css',
                chunkFilename: 'css/[name].[contenthash:8].css',
            })
        ]
}