import lightning as L
import torch
import torch.nn as nn


class pretrainedModel(L.LightningModule):
    def __init__(
        self, pre_trained_model, last_layer_classifier, loss_fn=nn.BCEWithLogitsLoss
    ):
        super().__init__()
        self.features = nn.Sequential(*list(pre_trained_model.children())[:-1])
        self.class_classifier = last_layer_classifier
        self.loss_fn = loss_fn()

    def forward(self, x):
        return self.class_classifier(self.features(x).view(x.size(0), -1))

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.loss_fn(y_hat, y)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=1e-3)

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.loss_fn(y_hat, y)
        return loss
