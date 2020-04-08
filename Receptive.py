net_struct = {'Conv-TasNet': {'net': [[3, 1, 0, 1], [3, 1, 0, 1], [2, 2, 0, 1], [3, 1, 0, 1], [3, 1, 0, 1], [2, 2, 0, 1], [3, 1, 0, 1], [3, 1, 0, 1], [2, 2, 0, 1], [3, 1, 0, 1], [3, 1, 0, 1], [2, 2, 0, 1], [3, 1, 0, 1], [3, 1, 0, 1], [2, 2, 0, 1],
                                      #[3, 1, 1, 1], [3, 1, 2, 2], [3, 1, 4, 4], [3, 1, 8, 8], [3, 1, 16, 16], [3, 1, 32, 32], [3, 1, 64, 64], [3, 1, 128, 128],
                                      [3, 1, 1, 1], [3, 1, 2, 2], [3, 1, 4, 4], [3, 1, 8, 8], [3, 1, 16, 16], [3, 1, 32, 32], [3, 1, 64, 64], [3, 1, 128, 128],
                                      [3, 1, 1, 1], [3, 1, 2, 2], [3, 1, 4, 4], [3, 1, 8, 8], [3, 1, 16, 16], [3, 1, 32, 32], [3, 1, 64, 64], [3, 1, 128, 128]],
                              'name': ['d1-conv1', 'd1-conv2', 'd1-down', 'd2-conv1', 'd2-conv2', 'd2-down', 'd3-conv1', 'd3-conv2', 'd3-down', 'd4-conv1', 'd4-conv2', 'd4-down', 'd5-conv1', 'd5-conv2', 'd5-down',
                                       'sep-1:conv1', 'sep-1:conv2', 'sep-1:conv3', 'sep-1:conv4', 'sep-1:conv5', 'sep-1:conv6', 'sep-1:conv7', 'sep-1:conv8',
                                       'sep-2:conv1', 'sep-2:conv2', 'sep-2:conv3', 'sep-2:conv4', 'sep-2:conv5', 'sep-2:conv6', 'sep-2:conv7', 'sep-2:conv8',
                                       'sep-3:conv1', 'sep-3:conv2', 'sep-3:conv3', 'sep-3:conv4', 'sep-3:conv5', 'sep-3:conv6', 'sep-3:conv7', 'sep-3:conv8']}}

imsize = 32000


def outFromIn(isz, net, layernum):
    totstride = 1
    insize = isz
    for layer in range(layernum):
        fsize, stride, pad, dilation = net[layer]
        outsize = (insize - dilation*(fsize-1) + 2*pad - 1) / stride + 1
        insize = outsize
        totstride = stride
    return outsize, totstride


def inFromOut(net, layernum):
    RF = 1
    for layer in reversed(range(layernum)):
        fsize, stride, pad, dilation = net[layer]
        RF = ((RF - 1) * stride) + dilation*(fsize - 1) + 1
    return RF


if __name__ == '__main__':
    print("layer output sizes given image = %dx%d" % (imsize, imsize))

    for net in net_struct.keys():
        print('************net structrue name is %s**************' % net)
        for i in range(len(net_struct[net]['net'])):
            p = outFromIn(imsize, net_struct[net]['net'], i+1)
            rf = inFromOut(net_struct[net]['net'], i+1)
            print("Layer Name = %s, Output size = %3d, Stride = % 3d, RF size = %3d" % (net_struct[net]['name'][i], p[0], p[1], rf))
